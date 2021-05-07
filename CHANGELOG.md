# Changelog

## [v2.3.4.dev0]

### Added
- [Core] Allow to execute a Class as lithops function
- [CE] Allow to to run code engine without kubecfg file

### Changed
- [CE] CPU and memory values must match predefined flavors

### Fixes
- [Core] Clear only present jobs instead of all after wait() or get_result()


## [v2.3.3]

### Fixes
- [Core] Allow to execute class methods as lithops function


## [v2.3.2]

### Added
- [Core] New "warm_container" and "func_result_size" in future statistics
- [Core] New logic to detect referenced modules/libs

### Changed
- [Core] New monitoring system
- [Core] Deleted strong dependency to pika==0.13.1

### Fixes
- [Partitioner] Fixed partitioner when obj url contains more than one subfolder
- [Cli] Fixed serverless runtime lifecycle methods

### Deleted
- [Core] Removed cloudpickle from lithops.libs


## [v2.3.1]

### Added
- [Core] Allow Support for Python 3.9
- [Core] Added standalone get_result() and wait() methods
- [knative] Include GCP and Azure storage libs into default knative runtime
- [CodeEngine] Enable internal kubernetes pod executions
- [k8s] Enable internal kubernetes pod executions
- [Cli] Added 'empty' function to storage cli to empty a bucket
- [Core] Added new method to FunctionExecutor() to calculate execution costs
- [IBM CF] Added formula to calculate execution costs
- [Multiprocessing] Added Nanomsg connection type for addressable backends
- [Multiprocessing] Added expiry time for Redis multiprocessing resources
- [Multiprocessing] Added Listener and Client for multiprocessing using Redis
- [Azure Functions] Added support for http trigger
- [Core] Set lithops to localhost mode when config files is empty

### Changed
- [IBM CF] Change user_key to API-key pass instead of user
- [Azure] Changed configuration keys
- [Core] Improved worker when chunksize is set to values > 1
- [Core] Check lithops version mismatch in host instead of in worker

### Fixes
- [Core] Overwrite the runtime set in config with the runtime set in the FunctionExecutor
- [Cli] Fixed --config param in lithops cli
- [Standalone] Fixed internal executions
- [Core] Fixed rabbitmq monitor when get_result() is called after wait()
- [GCP Storage] Fix GCP Storage backend put obj as stream
- [GCP Functions] Improved runtime create time
- [Azure blob] Fix in azure blob get method
- [Azure Functions] Fix build runtime command


## [v2.3.0]

### Added
- [Core] Added multiprocessing support in workers
- [Core] Added 'cunksize' param to API calls
- [Core] Added 'worker_processes' param to API calls
- [Core] Allow a worker to process more than one call trough 'chunksize' param
- [Core] All Functions logs are now synchronized with the client
- [Config] Allow 'log_level' and 'log_format' keys in configuration
- [Config] Allow 'log_stream' and 'log_filename' keys in configuration
- [Config] Allow 'runtime' being configured at serverless backend level
- [Config] Allow 'invoke_pool_threads' being configured at serverless backend level
- [Multiprocessing] Added generic Manager 
- [Kubernetes] Add kubernetes job backend
- [CLI] Extended lithops cli with storage put, get, delete and list options
- [Azure] Added missing azure functions backend methods

### Changed
- [Core] Improved Standalone execution mode
- [Core] Renamed utils.setup_logger() method to utils.setup_lithops_logger()
- [Core] Renamed partitioner 'chunk_size' param to 'obj_chunk_size'
- [Core] Renamed partitioner 'chunk_n' param to 'obj_chunk_number'
- [GCP Cloud Run] Refactor backend, removed 'gcloud' CLI calls.
- [IBM VPC] Improved IBM VPC backend
- [AWS Lambda] Lambda layer modules update

### Fixes
- [Multiprocessing] Fix issues related to Pipes and Queues
- [Multiprocessing] Fix multiprocessing.context methods
- [CodeEngine/knative] Fix getting docker username in MAC OS hosts


## [v2.2.15]

### Added
- [Joblib] Joblib backend upgraded
- [AWS Lambda] Support for container-based runtimes
- [AWS Lambda] Support for running functions in a VPC
- [AWS Lambda] Support for attaching EFS volumes
- [Core] Added cloudpickle, tblib and ps-mem deps as requirement of the runtimes
- [Core] Add a new Serverless mode that allows to include the function within the runtime

### Changed
- [Core] Allow Standalone mode to start 1 VM per activation

### Fixed
- [Core] Fixed issue in clean when it is called between wait and get_result
- [Core] Fixed multiprocessing Queue and get_context
- [Core] Fixed multiprocessing args mapping in map and map_async
- [Localhost] Fixed issue when using docker images in Windows or MAC

### Deleted
- [Core] Removed tblib from lithops.libs
- [Core] Removed ps-mem from lithops.libs

### Required actions
- Run: python3 -m pip install -U cloudpickle tblib ps-mem ibm-vpc namegenerator


## [v2.2.14]

### Added
- [Azure] Azure Functions backend upgraded
- [Azure] Azure blob backend upgraded
- [Alibaba] Alibaba Functions backend upgraded
- [Alibaba] Alibaba Storage backend upgraded
- [Localhost] Support passing file-like objects to put_object
- [Localhost] Support head_bucket and head_object storage operations

### Changed
- [Core] Moved tests.py script to 'scripts' folder

### Fixed
- [Core] Fixed Storage API error when no config is provided
- [Core] Fixed expired IAM token in IBM CF during an execution
- [Core] Minor fixes in multiprocessing API
- [Core] Fixed executor logging
- [Core] Fixed issue in cleaner between wait and get_result
- [CodeEngine] Fixed issue getting region
- [Localhost] Fixed empty parent directory deletion when deleting objects
- [Localhost] Made list_keys/list_objects behavior consistent with other backends


## [v2.2.13]

### Added
- [CodeEngine] Compatible runtimes between knative and CE
- [CodeEngine] runtime name regex verification
- [CodeEngine] Added clear() method to delete all completed jobruns
- [Standalone] Append installation logs into /tmp/lithops/proxy.log

### Changed
- [Localhost] Run functions in processes instead of threads in Windows
- [CodeEngine] Reduced payload size
- [Core] Updated logging

### Fixed
- [Core] Fixed Cloudpickle 1.6 modules detection
- [Core] Added tblib.pickling_support in the local machine


## [v2.2.11]

### Changed
- [CodeEngine] Delete runtime name regex verification


## [v2.2.10]

### Added
- [Core] Allow to create a Storage() class from config file
- [CodeEngine] Improved codeengine backend

### Changed
- [Core] Improved multiprocessing API
- [Core] Improved Storage OS API


## [v2.2.9]

### Fixed
- [CodeEngine] Fixed CodeEngine runtime entrypoint


## [v2.2.8]

### Fixed
- [Core] Fix "lithops runtime create" cli
- [Core] Fixed missing executor_id variable in jobrunner


## [v2.2.7]

### Added
- [Core] Add joblib backend for scikit-learn
- [Cli] Add more config paramters in lithops cli
- [IBM COS] Add 'region' config param
- [Knative] Add 'min_instances', 'max_instances' and 'concurrency' config params

### Fixed
- [Core] Fix job monitoring on Windows hosts
- [Knative] Minor fix when using knative from master branch
- [GCE] Fix in 'lithops runtime' cli
- [Core] Minor fix in tests
- [Core] Fixed data partitioner


## [v2.2.5]

### Fixed
- [Core] Fixed issue in serverless config
- [Core] Fixed issue in localhost storage backend
- [Code Engine] Fixed issue in code engine backend

## [v2.2.4]

### Added
- [Core] New 'lithops logs' command
- [Core] New job cleaner process

### Changed
- [Core] localhost/standalone logging per job-id
- [Core] Updated tblib to 1.7.0
- [Core] Updated ps_mem lib
- [Core] Standalone logic to ssh

### Fixed
- [Core] Fixed issue in localhost executor and Mac OS
- [Core] Fixed issue in localhost storage backend


## [v2.2.3]

### Added
- [Core] Cloudpickle 1.6.0 for python>=3.8
- [Core] Multiprocessing API
- [Core] Added "--mode" option in tests
- [Core] Sync standalone function logs into a local file

### Changed
- [Core] Improved localhost/standalone logging
- [Core] Allowed to run lithops without configuration

### Fixed
- [Core] Fixed some issues in localhost executor logic


## [v2.2.2]

### Fixed
- [Core] Prevent lithops waiting forever for the proxy ready
- [Core] Multiprocessing invoker in MAC OS
- [Knative] Istio endpoint issue in knative backend


## [v2.2.1]

### Changed
- [Core] Improved standalone executor logic
- [Knative] Updated apiVersion to v1
- [Knative] Updated default python3.8 Dockerfile

### Fixed
- [Core] Fixed runtime_memory param in API calls
- [Core] Raise fn exceptions immediately when produced
- [Core] Raise exceptions during fn invocation
- [IBM COS] Get tokens for IAM API key and COS API Key
- [AWS Lambda] Fixes in Lambda compute backend


## [v2.2.0]

### Added
- [Core] New ServerlessExecutor
- [Core] New StandaloneExecutor
- [Core] New LocalhostExecutor
- [Core] New StandaloneExecutor logic
- [Core] New LocalhostExecutor logic
- [Core] New Standalone invoker logic
- [Core] New Localhost invoker logic

### Changed
- [Core] Changed some main keys in configuration


## [v2.1.1]

### Changed
- [CodeEngine] Improved Code engine backend


## [v2.1.0]

### Added
- [Core] Google Cloud Functions & Storage backends
- [Core] Azure Functions & Blob Storage backends
- [Core] AWS Lambda & AWS S3 backends
- [Core] Alibaba Aliyun Functions & Object Storage backends
- [Core] IBM Code Engine Compute backend


## [v2.0.0]

### Changed
- [Core] Rebranding to LITHOPS


## [v1.7.3]

### Added
- [Core] Generic compute client logic
- [Core] IBM IAM service client lib
- [Core] IBM VPC service client lib
- [Docker] Docker backend compatible with IBM VPC VM 

### Fixed
-  [Ceph] Fix in ceph endpoint

### Changed
-  [Docker] Improved Docker executor


## [v1.7.2]

### Added
- [GCR] Added Google Cloud Run Backend

### Fixed
- [Core] Fixed invoker token bucket when quota limit is reached
- [Core] Fixed logging
- [Core] Fixed invoker when it reaches quota limit
- [Core] Fixed delete cloudobject
- [Localhost] Fixed invocations ability to launch subprocesses
- [Docker] Fixed docker running as user and not root

### Changed
- [Core] Improved Storage abstraction
- [Core] InternalStorage uses storage abstraction


## [v1.7.0]

### Added
- [GCS] Added Google Cloud Storage Backend
- [Knative] Configurable CPU parameter

### Fixed
- [Core] Fixed issue in extra_args when iterdata is a dict
- [Core] Fixed CloudObjects keys collisions
- [Core] Fixed case where function argument is a list or tuple


## [v1.6.0]

### Added
- [Core] New docker_executor()
- [Ceph] New Ceph Storage backend

### Changed
- [Core] Moved all stats from 'f._call_status' to a new 'f.stats' variable
- [Core] Bump httplib2 from 0.13.0 to 0.18.0
- [Localhost] Improved localhost storage backend

### Fixed
- [Core] Fixed issue in pw.clean(cs=cobjs) when passing a large list of cobjs


## [v1.5.2]

### Added
- [Core] Added 'data_limit' config param in pywren section
- [Core] Added context-manager-like executor and example
- [Core] Added debug mode in tests with '-d' flag
- [Core] Added delete_cobject() and delete_cobjects() storage methods

### Changed
- [Core] Reducer logic moved to jobrunner
- [Core] cloudobject methods moved from internal_storage to ibm_cos
- [Core] renamed cloudobject put method from 'put_object' to 'put_cobject'
- [Core] renamed cloudobject get method from 'get_object' to 'get_cobject'
- [Core] 'internal_storage' func param renamed to 'storage'
- [Core] pw.clean method can now clean cloudobjects
- [Knative] Set default Knative runtime timeout to 10 minutes
- [Knative] Added more debug logs in Knative
- [Knative] Enabled building default knative runtime locally

### Fixed
- [Core] Fixed issue in map_reduce() method
- [Core] Fixed issue in plot() method when using numpy 1.18.1
- [Core] Fixed issue in cloudpickle when iterdata contains complex objects
- [Core] Fixed issue with extra_env vars passed to functions
- [Core] Fixed issue in memory monitor
- [Core] Fixed issue in pywren-ibm-cloud cli
- [Core] Fixed issue when wait()/get_result() methods are called multiple times
- [Core] Fixed minor issue with ps_mem module in windows hosts
- [Knative] Fixed knative to pass all tests
- [Knative] Fixed remote_invoker in knative
- [Knative] Fixed issue when pywren version mismatch in Knative
- [Knative] Fixed issue in Knative when the default runtime is built
- [knative] Fixed building default runtime based on current python version
- [knative] Fixed OOM exceptions from knative to be correctly raised
- [IBM COS] Fixed issue when using local_executor with IBM COS authorized by an api_key


## [v1.5.1]

### Changed
- [Core] pw.create execution_plots() renamed to pw.plot()
- [Core] Docs updated

### Fixed
- [Core] Fixed internal issues
- [knative] Fixed minor issue in knative


## [v1.5.0]

### Added
- [Core] Added support for Python 3.8
- [Core] Added memory monitor

### Changed
- [Core] Updated knative to work for new releases
- [Core] Updated tblib from 1.4.0 to 1.6.0
- [Core] Changed get_current_memory_usage() to get_memory_usage()
- [Core] pywren-runtime client is now called pywren-ibm-cloud

### Fixed
- [Core] Fixed issue with internal partitioner
- [Core] Fixed issue with get_result()
- [Core] Fixed issue with windows hosts
- [Core] Some other Internal fixes

## [v1.4.2]

### Added
- [Core] Prevent get_result() to wait forever when using COS
- [Core] Added more debug logs
- [Infinispan] Infinispan storage backend

### Changed
- [Core] Reduced the number of COS clients created in each function activation

### Fixed
- [Core] Fixed internal issue with storage
- [Core] Fixed future exception handling
- [Core] Some other Internal fixes


## [v1.4.1]

### Added
- [Core] Prevent get_result() to wait forever when using RabbitMQ
- [knative] Added new Dockerflies for knative

### Changed
- [Core] Changed way to raise function exceptions
- [Knative] Changed way to build custom runtimes for knative
- [IBM CF] COS private_endpoint is now mandatory if using IBM CF

### Fixed
- [Knative] Fixed knative when it creates a runtime based on an already built image
- [Core] Fixed throw_except parameter on wait() and get_result()
- [Core] Some other Internal fixes


## [v1.4.0]

### Added
- [Core] New way to create RabbitMQ resources

### Changed
- [Core] Default invoker background processes set to 2
- [Core] Code refactoring

### Fixed
- [Core] Fixed issue when config in runtime is used multiple times
- [Core] Fixed invoker stop() method
- [Core] Some other Internal fixes


## [v1.3.1]

### Added
- OpenWhisk Compute backend
- openwhisk_executor()
- Allowed multiple users in same CF namespace
- Added IBM COS request retrying when ReadTimeoutError

### Changed
- COS token will expire 10 minutes before
- CF IAM token will expire 10 minutes before
- Improved remote invoker
- Reraise exception from functions
- Docs updated
- Default runtime timeout set to seconds
- default function timeout set to 595 secs

### Fixed
- Fixed new invoker usage in notebooks
- fixes in knative backend
- Some other Internal fixes


## [v1.3.0]

### Added
- New invoker mechanism
- New native remote invoker for ibm_cf
- pywren-runtime clean command to delete all tmp data
- capacity to limit the number of concurrent workers
- architecture documentation

### Changed
- Changed Internal data cleaner logic to delete only desired job
- Updated ibm_cf Dockerfiles
- Moved chunk min size from 1MB to 0MB
- changed executor id format
- Timeout waiting for functions to complete set to None by default
- Updated ibm_cf base image requirements

### Fixed
- Internal fixes
- Fixed tests
- Fixed pywren inside pywren function executions


## [v1.2.0]

### Added
- New local_executor() to run pywren jobs in the local machine
- New localhost compute backend
- New localhost storage backend
- New docker_executor() to run pywren jobs in the local machine by using docker
- New docker compute backend

### Changed
- Docs updated
- Code refactor

### Fixed
- Internal fixes
- Bump pillow from 5.4.1 to 6.2.0


## [v1.1.1]

### Added
- Allowed partitioner to split files by a number of chunks
- Missing logic in knative backend

### Changed
- Docs updated

### Fixed
- Internal fixes


## [v1.1.0]

### Added
- Added knative-serving compute backend
- Added Dockerfile skeleton for slim Python3.6 runtime (only 307MB)
- Added CACHE_DIR in ~/.pywren/cache
- knative_executor() and function_executor()
- support to work on multiple regions at a time

### Changed
- Docs updated
- Runtime Dockerfiles updated
- Runtime requirements updated
- Updated Cloudpickle lib to version 1.2.2
- Parameters introduced in the executer now overwrite the config
- updated tests

### Fixed
- Internal logic to generate runtime_metadata
- invalid call to "is_remote_cluster" method
- Cloudpickle lib to accept any kind of import
- include_modules option in serializer


## [v1.0.20]

### Added
- Storage abstraction for data partitioner
- Added 'extra_params' arg to map() and map_reduce() calls
- Logic to reuse IAM API Key tokens during 1 hour
- More debug logging

### Changed
- Docs updated
- Full support for Python3.5

### Fixed
- Fixed minor issue in config
- Fixed possible issue extracting metadata from large docker images (runtimes)


## [v1.0.19]

### Added
- Added 'obj' as an optional arg for the functions when a user wants to process objects from OS
- Added 'rabbitmq' as an optional arg for the functions
- Added 'id' as an optional arg for the functions
- Added rabbitmq example

### Changed
- Deleted 'bucket' 'key' 'data_stream' function args in favor of 'obj'
- Internal improvements related data partitioning
- Changed create_timeline_plots() method name to create_execution_plots()
- Docs updated
- updated notebooks
- Upgrade cos-sdk Python module version

### Fixed
- Fixed tests
- Fixed CVE-2019-12855 security alert


## [v1.0.18]

### Added
- Added CloudObject abstraction
- Added CloudObject example
- Restored OOM exception
- Allowed to get_results when rabbit monitoring is activated
- Allowed rabbimq to monitor multiple jobs at a time
- Statuses returned from rabbitmq to futures

### Changed
- Code refactoring about compute abstraction
- Reorganized libs folder
- Updated cloudpickle lib from 0.6.1 to 1.2.1
- Updated glob2 lib to 0.7
- Updated tests
- Modified job_id format

### Fixed
- Fixed minor issue listing CF actions
- Fixed issue when executing pywren inside pywren
- Fixed possible issue with invalid config parameters
- Fixed wrong method name: build_runtime()
- Fixed internal_storage parameter in partitioner
- Fixed crete_timeline_plots method according recent changes


## [v1.0.17]

### Changed
- Code refactoring about compute abstraction

### Fixed
- Fixed issue with invocation retries


## [v1.0.16]

### Added
- Added missing init file
- Allowed 'clean=all' arg in clean() method

### Changed
- Simplified invoker
- Moved compute and storage classes to separate files
- Deleted unnecessary files
- Close plots on finish
- Code refactoring about compute abstraction

### Fixed
- Fixed broken readme links
- Fix in invocation method


## [v1.0.15]

### Added
- Added log information
- Added init files
- Store runtime_metadata into a local cache in order to reduce exec time

### Changed
- Modularized Invoker
- Changed some variable names
- Docs updated

### Fixed
- Fixed set_memory in invoker
- Fixed unneeded memory usage
- Fixed none finished futures
- Fixed wait method
- Fixed issue with map_reduce()


## [v1.0.14]

### Added
- Pywren runtime deployment as script
- Changed name of the runtime deployment script
- Added 'pywren_runtime clean' option
- Added function_name and runtime_memory to future's status
- Added 'pywren_runtime update all' option
- Added exception when preinstalled modules list is not well provided
- Add package parameter to delete function

### Changed
- Improved sending execution statuses through rabbitmq
- Improved exception management
- Moved some logs to debug
- Improved runtime deployment script
- Changed logic order of the create_timeline_plots method

### Fixed
- Preventing false out-of-memory error
- Fixed issue when using rabbitmq to monitor executions
- Fixed issue tracking map_reduce execution with progressbar
- Some other fixes


## [v1.0.13]

### Changed
- match create_timeline_plots() to rabbitmq feature

### Fixed
- Fixed possible issue deploying runtime
- Fixed jobrunner logs
- Fix in url paths
- Some other fixes


## [v1.0.12]

### Changed
- Moved ibm_iam lib from tornado to requests package
- Minor change create_timeline_plots()

### Fixed
- Map futures before reduce wont be downloaded
- Fix in cf_connector
- Fix in tests
- private endpoint fix
- Some other fixes


## [v1.0.11]

### Added
- Support for IBM IAM authentication for IBM CF and IBM COS
- Take into account cf_region and cf_namespace in runtime_name

### Changed
- Improved invocation speed
- Improved runtime deployment
- Minor improve get_result()
- Moved 'create action name' logic to utils
- Change map_reduce to return also map futures
- Improved remote_invocation mechanism
- Moved cf_connector to libs

### Fixed
- Fixed deploy_utils script
- Some other fixes


## [v1.0.10]

### Added
- Add support to create pywren's plots in cos

### Fixed
- Fixed future status
- Fixed wait method
- Fixed minor issues in plots.py and wren.py
- Clarified when future is ready or done
- Some other fixes


## [v1.0.9]

### Added
- Added COS private_endpoint parameter
- added external config support for tests' executors
- Added exceptions management in monitor() method

### Changed
- integrated test file into PyWren
- Tuned-up some parameters
- Send jobrunner config through a parameter
- docs verify section update
- moved test call outside of wren.py

### Fixed
- Fixed issues when PyWren is used from a Windows host
- Fixed issue with 'signal' module on Windows hosts
- Check token timestamp of COS


## [v1.0.8]

### Added
- Added connection timeout on COS to avoid possible issues

### Fixed
- Fixed possible issue when calling future.result()
- Some other fixes


## [v1.0.7]

### Added
- Runtimes automatically created

### Changed
- Improved Runtime management
- Improved performance of jobrunner
- Updated notebooks
- Restored .gitignore
- Docs updated

### Fixed
- Some minor fixes


## [v1.0.6]

### Added
- Enabled memory configuration in the executor

### Changed
- Docs updated

### Fixed
- Fix issue in cf_connector
- Some other fixes


## [v1.0.5]

### Added
- log_level propagated to functions
- added an option to get debug logs from boto3
- Support for configurable IAM endpoint
- added chunk_size tests

### Changed
- Project structure refactor
- Modified create_zip_action method
- Docs updated
- Improved runtime deployment
- improved 'bucket' parallelism in partitioning
- Removed annoying info prints

### Fixed
- Fix function name
- Fixed issue in cf_connector when running PW from Windows
- Fix issue with log_level
- Fixed issue with white spaces when deploying a runtime


## [v1.0.4]

### Added
- Added rabbitmq logic
- Added is_notebook method
- Added wrapper to data_stream for partitioned data
- Created WrappedStreamingBodyPartition() class for data partitions
- Run multiple maps() in the same executor
- added multiple execution on the same executor tests
- added ibm_cos tests
- Added download_results parameter in monitor() method to ensure all results are downloaded
- Added pika package to dependencies
- Tracking new futures from a function
- Example of Docker image for dlib

### Changed
- Change name of wait() method to monitor()
- Tuned up some parameters to speedup wait method
- Moved all partitioner logic into partitioner.py
- Installation script to support PW version as a parameter
- Changed way to get last row position on data partition
- Deleted duplicated get_result method
- Hide urllib3 annoying debug logs within functions
- Activate remote_invocation when data comes from COS
- Docs updated

### Fixed
- Fixed partitioner data wrapper
- Fix tests to work with last partitioner update
- Fixed chunk threshold
- Fix printing plots
- Fixed rabbitmq config
- Some other fixes


## [v1.0.3]

### Added
- Add support to generate execution timeline plots
- pi_estimation_using_monte_carlo_with_PyWren.ipynb
- stock_prediction_monte_carlo_with_PyWren.ipynb
- Added missing modules in setup.py
- Added memory usage in action logs

### Changed
- Reverted cloudpickle usage
- Move default action memory to 512MB
- Improved installation script
- Refactored deploy_runtime script
- Updated deploy_runtime script, clone command
- Docs updated
- Finished map() and map_reduce() consistency issue
- Raise exception when some activation fails

### Fixed
- Fixed issue reusing COS tokens
- Fixed partitioner object split
- Fixed map() and map_reduce() consistency issue
- Some other fixes


## [v1.0.2]

### Added
- ibm_boto3 client as an input of the parameter 'ibm_cos' of the function
- Add functional test script
- Added retry logic
- Invoker logic
- Added missing init file
- Added user agent to identify pywren
- Added missing dependencies

### Changed
- Abstracted COS logic for map() and map_reduce() methods
- pw.map() method through COS abstractions
- Retry mechanism when exception
- Use CloudPickle module in all project for serializing/unserializing
- Docs updated
- Storage separation
- Project update. 'bx' and 'wsk' CLI tools are no longer necessary
- Updated setup.py 
- Deleted requirements.txt 
- Updated default_preinstalls

### Fixed
- Minor warnings fix
- Fixed logging
- step back with gevent until import fixed in openwhisk
- Fixed issue when running map_reduce job from COS keys
- Fixed issue retrieving results
- Fixed issue when processing a dataset from url
- Fixed issue when running map_reduce method
- Some other fixes


## [v1.0.1]

### Added
- Example of the Docker image that is based on Anaconda
- Enabled support for multiple call_assync() calls in the same pw instance
- Added 'OutOfMemory' Exception
- Jupyter notebook example
- configurable cleaner for temporary data

### Changed
- Changed and improved logging in order to log correctly within IBM Cloud Functions
- Changed Python interpreter of the data_cleaner method
- Moved some info prints to debug
- improved remote function invocation mechanism

### Fixes
- Fixing flask security issues CVE-2018-1000656
- Fixed minor issue when futures is not a list
- Fixed default config exception. API KEY is not mandatory.
- Fixes in logging
- Some other fixes


## [v1.0.0]
First release.

- New runtime based on Docker images.
- Added IBM Cloud Functions API connector for function invocations.
- Added support for IBM Cloud Object Storage (COS) backend (or S3 API).
- Added support for OpenStack Swift backend (or Swift API).
- Added timeout while PyWren is getting the results. It prevents PyWren waits forever when some function fails and the results are not stored in COS.
- Created the ibmcf/default_config.yaml config file for storing the main PyWren configuration parameters such as Cloud Functions and COS access keys.
- Enabled to use PyWren within a PyWren function.
- Enabled redirections. Now it is possible to send a *Future* class as a response of a function. This means that the function has executed another function, and the local PyWren has to wait for another response from another invocation.
- Added a new **map_reduce()**-like method: Unlike the original **map** and **reduce** methods, this new one integrates an automatic data partitioning based on a chunk size provided by the user. Both the **map** and the **reduce** functions are orchestrated and executed within Cloud Functions and the user just waits for the final result provided by the reduce function.
- Automatic data discovering in the new **map_reduce()**-like method. With this method it is possible to specify a bucket name in order to process all the objects within it instead of specifying each object one by one.
- Created a function which removes residual data from COS when the PyWren execution finishes.
- The main **executor** is a *class* and not a *method*.
- All the methods available for the users are integrated within the main *executor class*.
- Added state in the main *executor class* in order to control the correct execution order of its methods (like a Turing machine)
- When a new *executor class* is instantiated, it is created a new unique **executor_id** used to store all the objects in COS, and to retrieve the results.
- When a new *executor class* is instantiated, it is created a *storage_handler* used in the all PyWren execution.
- Now it is possible to specify the **runtime** when the user instantiates the *executor class* instead of changing the config file every time (In the config file is specified the default runtime).
- The **logging level** is now specified when the user instantiates the *executor class* instead of put it in the first line of the code within an env variable.
- The PyWren code which is executed remotely as a wrapper of the function now uses the main storage handler as the rest of the PyWren code. In previous versions, PyWren creates a new storage client directly with *boto3* library instead of using pywren/storage/storage.py wrapper. 
- Added support for multiple parameters in the functions which are executed remotely as a cloud functions. Previous versions just allows one parameter.
- Eased the usage of the storage backend within a function. By simply specifying *storage_handler* as a parameter of the function, the user will get access to the storage backend.
- Added a new method for retrieving the results of an execution called **fetch_all_resuslts()**. Previous PyWren versions already includes a method called *get_all_results()*, but this is a sequential method and it takes long time to retrieve all the results. It was also included a *wait()* class which is more similar to *get_all_results()* method, the main difference is that the new method is all based on *list the available objects in a bucket*, and it returns when all the tasks are finished. The new method also has the possibility to activate a progress bar in order to track the current status of the execution (really useful for larger executions).
- Added support for libs not included in the IBM Cloud Functions native image (*python-jessie:3*). Some libraries necessary for executing PyWren (remote code) are not included in the native CFs docker image. Now PyWren has the *pywren/libs* dir which includes all of these libraries, so it is possible to use PyWren with the native Docker image instead of building a new one with the missing libraries.
- In the COS backend, the *boto3* library was changed to the *ibm_boto3* library
- Increased function execution timeout to 600 seconds (10 minutes)
- Other minor changes