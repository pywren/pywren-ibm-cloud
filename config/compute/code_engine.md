# Lithops on IBM Code Engine

[IBM Code Engine](https://cloud.ibm.com/codeengine/overview) allows you to run your application, job or container on a managed serverless platform. Auto-scale workloads and only pay for the resources you consume.

IBM Code Engine exposes both Knative and Kubernetes Job Descriptor API. Lithops supports both of them. Follow IBM Code Engine documentation to get more details on the difference between those APIs.

###  Installation

#### Option 1 (IBM CLoud Dashboard):
1. Navigate to the [IBM Cloud Code Engine dashboard](https://cloud.ibm.com/codeengine/landing) and create a new project in your preferred region.


#### Option 2 (IBM CLoud CLI tool):
In this step you are required to install IBM Cloud CLI tool, Code Engine plugin and create new Code Engine project

1. Install the [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started):

   ```bash
   curl -sL https://ibm.biz/idt-installer | bash
   ```

2. Login to your account, pointing to the region you want to create a project

   ```bash
   ibmcloud login -r us-south
   ```

3. Install the IBM Code Engine plugin:

   ```bash
   ibmcloud plugin install code-engine
   ```

4. Create a new Code Engine project (you can also do this through the dashboard). If you already have an existing project, then proceed to step 5:

   ```bash
   ibmcloud ce project create --name myproject
   ```

5. Target to your project:

   ```bash
   ibmcloud ce project select --name myproject
   ```
  
### Configuration

#### Option 1 (IBM IAM):
1. If you don't have an IAM API key created, navigate to the [IBM IAM dashboard](https://cloud.ibm.com/iam/apikeys).

2. Click `Create an IBM Cloud API Key` and provide the necessary information.

3. Copy the generated IAM API key (You can only see the key the first time you create it, so make sure to copy it).

4. Locate your project namespace name.

5. Edit your lithops config and add the following keys:
    ```yaml
    serverless:
        backend: code_engine
        
    ibm:
        iam_api_key: <IAM_API_KEY>
       
    code_engine:
        namespace  : <NAMESPACE>
        region     : <REGION>
    ```

#### Option 2 (KUBECONFIG file):

1. Locate the kubernetes config file using the IBM CLoud CLI:

   ```bash
   ibmcloud ce project current
   ```

2. Set or copy the KUBECONFIG environment variable as printed in the previous step:

   ```bash
   export KUBECONFIG=<PATH TO YAML FILE>
   ```

3. Edit your lithops config and add the following keys:
    ```yaml
    serverless:
        backend: code_engine
       
    code_engine:
        kubecfg_path: <PATH TO CONFIG YAML FILE>
    ```

### Runtime

To work with Code Engine there is need to use dedicated runtime. Lithops automatically builds the default runtime the first time you run a script. For this task it uses the **docker** command installed locally in your machine. Alternatively, you can use a pre-built runtime listed below.

1. [Install the Docker CE version](https://docs.docker.com/get-docker/).

2. Login to your docker account:
   ```bash
   docker login
   ```

|Default runtime name| Python version | What is included | Lithops version |
|----|-----|----|-----|
|ibmfunctions/lithops-ce-3.7.5-2.2.0:1.0.0 | 3.7 | [included](../../runtime/code_engine/requirements.txt) | 2.2.0 |
|ibmfunctions/lithops-ce-3.8.5-2.2.2:1.0.0 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.2.2 |
|ibmfunctions/lithops-ce-3.8.5-2.2.9:1.0.0 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.2.9 |
|ibmfunctions/lithops-codeengine-v38:2213 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.2.13 |
|ibmfunctions/lithops-codeengine-v37-1:2213 | 3.7 | [included](../../runtime/code_engine/requirements.txt) | 2.2.13 |
|ibmfunctions/lithops-ce-v37:2216 | 3.7 | [included](../../runtime/code_engine/requirements.txt) | 2.2.16 |
|ibmfunctions/lithops-ce-v38:2216 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.2.16 |
|ibmfunctions/lithops-ce-v385:230 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.3.0 |
|ibmfunctions/lithops-ce-v370:230 | 3.7 | [included](../../runtime/code_engine/requirements.txt) | 2.3.0 |
|ibmfunctions/lithops-ce-v385:232 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.3.2 |
|ibmfunctions/lithops-ce-v385:233 | 3.8 | [included](../../runtime/code_engine/requirements.txt) | 2.3.3 |

If you need to create custom runtime, please follow [Building and managing Lithops runtimes to run the functions](../../runtime/)


### Summary of configuration keys for Job API:

|Group|Key|Default|Mandatory|Additional info|
|---|---|---|---|---|
|code_engine | namespace |  |no | Namespace name|
|code_engine | region |  | no | Cluster region. One of *us-south*, *jp-tok*, *eu-de*, *eu-gb* |
|code_engine | kubecfg_path | |no | Path to kubecfg file. Mandatory if config file not in `~/.kube/config` or KUBECONFIG env var not present|
|code_engine | container_registry |  docker.io | no | container registry url|
|code_engine | runtime |  |no | Docker image name.|
|code_engine | runtime_cpu | 0.125 |no | CPU limit. Default 0.125vCPU. See [valid combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo) |
|code_engine | runtime_memory | 256 |no | Memory limit in MB. Default 256Mi. See [valid combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo) |
|code_engine | runtime_timeout | 600 |no | Runtime timeout in seconds. Default 600 seconds |


### Lithops using Knative API of Code Engine

The only requirement to make it working is to have the KUBECONFIG file properly configured.


#### Edit your lithops config and add the following keys:

   ```yaml
   serverless:
       backend: knative
   ```

#### Summary of configuration keys for Knative:

|Group|Key|Default|Mandatory|Additional info|
|---|---|---|---|---|
|knative | kubecfg_path | |no | Path to kubecfg file. Mandatory if config file not in `~/.kube/config` or KUBECONFIG env var not present|
|knative | container_registry |  docker.io | no | container registry url|
|knative | docker_user | |no | Docker hub username |
|knative | docker_token | |no | Login to your docker hub account and generate a new access token [here](https://hub.docker.com/settings/security)|
|knative | git_url | |no | Git repository to build the image |
|knative | git_rev | |no | Git revision to build the image |
|knative | min_instances | 0 |no | Minimum number of parallel runtimes |
|knative | max_instances | 250 |no | Maximum number of parallel runtimes |
|knative | concurrency | 1 |no | Number of workers per runtime instance |
|knative | runtime |  |no | Docker image name.|
|knative | runtime_cpu | 0.125 |no | CPU limit. Default 0.125 vCPU. See [valid combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo) |
|knative | runtime_memory | 256 |no | Memory limit in GB. Default 256Mi. See [valid combinations](https://cloud.ibm.com/docs/codeengine?topic=codeengine-mem-cpu-combo) |
|knative | runtime_timeout | 600 |no | Runtime timeout in seconds. Default 600 seconds |

### Usage Example

```python
import lithops

iterdata = ['Gil', 'Dana', 'John', 'Scott']

def add_value(name):
    return 'Hello ' + name

if __name__ == '__main__':
    lt = lithops.FunctionExecutor(backend='code_engine', runtime='ibmfunctions/lithops-ce-v385:233')
    lt.map(add_value,  iterdata)
    print(lt.get_result())
```

###  Troubleshooting

#### Fault
Lithops throws exception with 'Missing access token parameter'

##### Cause / Remedy
This likely occurs when you were logout from ibmcloud or the kubectl token can't re-generate new authentication token. To resolve this login into ibmcloud and re-create kubectl file

    ibmcloud login -r <CE Project Region>
    ibmcloud target -g <GROUP> -o <ORG>
    ibmcloud ce project select --name <CPROJECT NAME> --kubecfg
