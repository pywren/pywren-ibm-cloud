#
# (C) Copyright IBM Corp. 2020
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys
import shutil

from lithops.utils import version_str, get_docker_username
from lithops.version import __version__

RUNTIME_NAME = 'lithops-codeengine'

CONTAINER_REGISTRY = 'docker.io'
DOCKER_PATH = shutil.which('docker')

RUNTIME_TIMEOUT = 600  # Default: 600 seconds => 10 minutes
RUNTIME_MEMORY = 256  # Default memory: 256 MB
RUNTIME_CPU = 0.125  # 0.125 vCPU
MAX_CONCURRENT_WORKERS = 1000
INVOKE_POOL_THREADS_DEFAULT = 4
DEFAULT_GROUP = "codeengine.cloud.ibm.com"
DEFAULT_VERSION = "v1beta1"

FH_ZIP_LOCATION = os.path.join(os.getcwd(), 'lithops_codeengine.zip')

VALID_CPU_VALUES = [0.125, 0.25, 0.5, 1, 2, 4, 6, 8]
VALID_MEMORY_VALUES = [256, 512, 1024, 2048, 4096, 8192, 12288, 16384, 24576, 32768]
VALID_REGIONS = ['us-south', 'jp-tok', 'eu-de', 'eu-gb']

CLUSTER_URL = 'https://proxy.{}.codeengine.cloud.ibm.com'

DOCKERFILE_DEFAULT = """
RUN apt-get update && apt-get install -y \
        zip \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools six pip \
    && pip install --no-cache-dir \
        gunicorn \
        pika \
        flask \
        gevent \
        glob2 \
        ibm-cos-sdk \
        redis \
        requests \
        PyYAML \
        kubernetes \
        numpy \
        cloudpickle \
        ps-mem \
        tblib

ENV PORT 8080
ENV CONCURRENCY 4
ENV TIMEOUT 600
ENV PYTHONUNBUFFERED TRUE

# Copy Lithops proxy and lib to the container image.
ENV APP_HOME /lithops
WORKDIR $APP_HOME

COPY lithops_codeengine.zip .
RUN unzip lithops_codeengine.zip && rm lithops_codeengine.zip

CMD exec gunicorn --bind :$PORT --workers $CONCURRENCY --timeout $TIMEOUT lithopsentry:proxy
"""

JOBDEF_DEFAULT = """
apiVersion: codeengine.cloud.ibm.com/v1beta1
kind: JobDefinition
metadata:
  name: "<INPUT>"
  labels:
    type: lithops-runtime
spec:
  arraySpec: '0'
  maxExecutionTime: 7200
  retryLimit: 3
  template:
    containers:
    - image: "<INPUT>"
      name: "<INPUT>"
      command:
      - "/usr/local/bin/python"
      args:
      - "/lithops/lithopsentry.py"
      - "$(ACTION)"
      - "$(PAYLOAD)"
      env:
      - name: ACTION
        value: ''
      - name: PAYLOAD
        valueFrom:
          configMapKeyRef:
             key: 'lithops.payload'
             name : NAME
      resources:
        requests:
          cpu: '1'
          memory: 128Mi
"""


JOBRUN_DEFAULT = """
apiVersion: codeengine.cloud.ibm.com/v1beta1
kind: JobRun
metadata:
  name: "<INPUT>"
spec:
  jobDefinitionRef: "<REF>"
  jobDefinitionSpec:
    arraySpec: '1'
    maxExecutionTime: 7200
    retryLimit: 2
    template:
      containers:
      - name: "<INPUT>"
        env:
        - name: ACTION
          value: ''
        - name: PAYLOAD
          valueFrom:
            configMapKeyRef:
              key: 'lithops.payload'
              name : ''
        resources:
          requests:
            cpu: '1'
            memory: 128Mi
"""


def load_config(config_data):
    if 'code_engine' not in config_data:
        config_data['code_engine'] = {}

    if 'kubectl_config' in config_data['code_engine']:
        print('"kubectl_config" variable in code_engine config is deprecated, use "kubecfg_path" instead')
        config_data['code_engine']['kubecfg_path'] = config_data['code_engine']['kubectl_config']

    if 'cpu' in config_data['code_engine']:
        print('"cpu" variable in code_engine config is deprecated, use "runtime_cpu" instead')
        config_data['code_engine']['runtime_cpu'] = config_data['code_engine']['cpu']

    if 'runtime_cpu' not in config_data['code_engine']:
        config_data['code_engine']['runtime_cpu'] = RUNTIME_CPU

    if 'container_registry' not in config_data['code_engine']:
        config_data['code_engine']['container_registry'] = CONTAINER_REGISTRY

    if 'ibm' in config_data and config_data['ibm'] is not None:
        config_data['code_engine'].update(config_data['ibm'])

    # shared keys
    if 'runtime' in config_data['code_engine']:
        config_data['serverless']['runtime'] = config_data['code_engine']['runtime']
    if 'runtime_memory' in config_data['code_engine']:
        config_data['serverless']['runtime_memory'] = config_data['code_engine']['runtime_memory']
    if 'runtime_timeout' in config_data['code_engine']:
        config_data['serverless']['runtime_timeout'] = config_data['code_engine']['runtime_timeout']

    if 'runtime_cpu' not in config_data['code_engine']:
        config_data['code_engine']['runtime_cpu'] = RUNTIME_CPU
    if 'runtime_memory' not in config_data['serverless']:
        config_data['serverless']['runtime_memory'] = RUNTIME_MEMORY
    if 'runtime_timeout' not in config_data['serverless']:
        config_data['serverless']['runtime_timeout'] = RUNTIME_TIMEOUT
    if 'runtime' not in config_data['serverless']:
        if not DOCKER_PATH:
            raise Exception('docker command not found. Install docker or use '
                            'an already built runtime')
        if 'docker_user' not in config_data['code_engine']:
            config_data['code_engine']['docker_user'] = get_docker_username()
        if not config_data['code_engine']['docker_user']:
            raise Exception('You must provide "docker_user" param in config '
                            'or execute "docker login"')
        docker_user = config_data['code_engine']['docker_user']
        python_version = version_str(sys.version_info).replace('.', '')
        revision = 'latest' if 'dev' in __version__ else __version__.replace('.', '')
        runtime_name = '{}/{}-v{}:{}'.format(docker_user, RUNTIME_NAME, python_version, revision)
        config_data['serverless']['runtime'] = runtime_name

    else:
        if config_data['serverless']['runtime'].count('/') > 1:
            # container registry is in the provided runtime name
            cr, rn = config_data['serverless']['runtime'].split('/', 1)
            config_data['code_engine']['container_registry'] = cr
            config_data['serverless']['runtime'] = rn

    runtime_cpu = config_data['code_engine']['runtime_cpu']
    if runtime_cpu not in VALID_CPU_VALUES:
        raise Exception('{} is an invalid runtime cpu value. Set one of: '
                        '{}'.format(runtime_cpu, VALID_CPU_VALUES))

    runtime_memory = config_data['serverless']['runtime_memory']
    if runtime_memory not in VALID_MEMORY_VALUES:
        raise Exception('{} is an invalid runtime memory value in MB. Set one of: '
                        '{}'.format(runtime_memory, VALID_MEMORY_VALUES))

    region = config_data['code_engine'].get('region')
    if region and region not in VALID_REGIONS:
        raise Exception('{} is an invalid region name. Set one of: '
                        '{}'.format(region, VALID_REGIONS))

    if 'workers' not in config_data['lithops'] or \
       config_data['lithops']['workers'] > MAX_CONCURRENT_WORKERS:
        config_data['lithops']['workers'] = MAX_CONCURRENT_WORKERS

    if 'invoke_pool_threads' not in config_data['code_engine']:
        config_data['code_engine']['invoke_pool_threads'] = INVOKE_POOL_THREADS_DEFAULT
    config_data['serverless']['invoke_pool_threads'] = config_data['code_engine']['invoke_pool_threads']
