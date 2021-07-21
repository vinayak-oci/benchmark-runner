#
# import time
# import pytest
#
# from benchmark_runner.common.oc.oc import OC
# from benchmark_runner.common.oc.oc_exceptions import PodNotCreateTimeout, PodTerminateTimeout, VMNotCreateTimeout, YAMLNotExist
# from benchmark_runner.common.elasticsearch.es_operations import ESOperations
# from benchmark_runner.main.update_data_template_yaml_with_environment_variables import delete_generate_file, update_environment_variable
# from benchmark_runner.benchmark_operator.benchmark_operator_workloads import BenchmarkOperatorWorkloads
# from tests.integration.benchmark_runner.test_environment_parameters import *
#
#
# def __generate_pod_yamls():
#     """
#     This method create pod yaml from template and inject environment variable inside
#     :return:
#     """
#     update_environment_variable(dir_path=templates_path, yaml_file='stressng_template.yaml', environment_variable_dict=environment_variable)
#
#
# def __generate_vm_yamls():
#     """
#     This method create vm yaml from template and inject environment variable inside
#     :return:
#     """
#     update_environment_variable(dir_path=templates_path, yaml_file='stressng_vm_template.yaml', environment_variable_dict=environment_variable)
#
#
# def __delete_pod_yamls():
#     """
#     This method delete pod yamls if exist
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.delete_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     delete_generate_file(full_path_yaml=os.path.join(f'{templates_path}', 'stressng.yaml'))
#
#
# def __delete_vm_yamls():
#     """
#     This method delete vm yamls if exist
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.delete_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#     delete_generate_file(full_path_yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'))
#
#
# @pytest.fixture(scope="session", autouse=True)
# def before_after_all_tests_fixture():
#     """
#     This method is create benchmark operator pod once for ALL tests
#     :return:
#     """
#     print('Install benchmark-operator pod')
#     benchmark_operator = BenchmarkOperatorWorkloads(kubeadmin_password=environment_variable['kubeadmin_password'],
#                                                     es_host=environment_variable['elasticsearch'],
#                                                     es_port=environment_variable['elasticsearch_port'],
#                                                     workload=environment_variable['workload'])
#     benchmark_operator.delete_benchmark_operator_if_exist()
#     benchmark_operator.helm_install_benchmark_operator(install_path=environment_variable['install_path'])
#     yield
#     print('Delete benchmark-operator pod')
#     benchmark_operator.helm_delete_benchmark_operator()
#
#
# @pytest.fixture(autouse=True)
# def before_after_each_test_fixture():
#     """
#     This method is clearing yaml before and after EACH test
#     :return:
#     """
#     # before all test: setup
#     __generate_pod_yamls()
#     __generate_vm_yamls()
#     yield
#     # After all tests
#     __delete_pod_yamls()
#     __delete_vm_yamls()
#     print('Test End')
#
#
# def test_login():
#     """
#     This method test login
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     # byte to string
#     result = oc.login().decode("utf-8")
#     assert 'Login successful' in result
#
#
# def test_oc_get_pods():
#     """
#     This method test get pods
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     assert oc.get_pods()
#
# def test_oc_get_pods():
#     """
#     This test run oc get pods
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     assert oc.get_pods()
#
#
# def test_oc_get_pod_name():
#     """
#     This test run oc get pod by name
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     assert oc._get_pod_name(pod_name='wcwcwcwc', namespace='my-ripsaw') == ''
#
# def test_oc_get_pod_name():
#     """
#     This method test get pod name
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     assert oc._get_pod_name(pod_name='benchmark-operator', namespace='my-ripsaw')
#
#
# def test_oc_is_pod_exist():
#     """
#     This method check if pod exist
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     assert oc._is_pod_exist(pod_name='benchmark-operator', namespace='my-ripsaw')
#
#
# def test_wait_for_pod_created():
#     """
#     This method wait for pod to be created
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc._create_async(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'))
#     assert oc.wait_for_pod_create(pod_name='stressng-workload')
#
#
# def test_create_pod_sync():
#     """
#     This method create pod synchronized
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     assert oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_oc_get_vmi_name():
#     """
#     This method wait for vm to be created
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc._create_async(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'))
#     # wait 30 sec till vm will be created
#     time.sleep(30)
#     assert oc._get_vmi_name(vm_name='stressng-vm-benchmark-workload', namespace='my-ripsaw')
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_oc_is_vmi_exist():
#     """
#     This method check if vm exist
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc._create_async(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'))
#     # wait 30 sec till vm will be created
#     time.sleep(30)
#     assert oc._is_vmi_exist(vm_name='stressng-vm-benchmark-workload', namespace='my-ripsaw')
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_wait_for_vm_created():
#     """
#     This method wait for vm to be created
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc._create_async(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'))
#     assert oc.wait_for_vm_create(vm_name='stressng-vm-benchmark-workload')
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_oc_get_vmi():
#     """
#     This method run get vmi
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#     assert oc.get_vmi()
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_create_vm_sync():
#     """
#     This method create vm synchronized
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     assert oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#
#
# def test_get_long_uuid():
#     """
#     This method test long uuid
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     assert len(oc.get_long_uuid()) == 36
#
#
# def test_get_sort_uuid():
#     """
#     This method test sort uuid
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     assert len(oc._OC__get_short_uuid()) == 8
#
#
# def test_delete_pod_sync():
#     """
#     This method delete pod synchronized
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     assert oc.delete_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_delete_vm_sync():
#     """
#     This method delete vm synchronized
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#     assert oc.delete_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#
#
# def test_yaml_file_not_exist_error():
#     """
#     This method create pod with timeout error
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     with pytest.raises(YAMLNotExist) as err:
#         oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng1.yaml'), pod_name='stressng-workload', timeout=0)
#
#
# def test_create_sync_pod_timeout_error():
#     """
#     This method create pod with timeout error
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     with pytest.raises(PodNotCreateTimeout) as err:
#         oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload', timeout=0)
#
#
# def test_delete_sync_pod_timeout_error():
#     """
#     This method delete pod with timeout error
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     with pytest.raises(PodTerminateTimeout) as err:
#         oc.delete_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload', timeout=0)
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_create_sync_vm_timeout_error():
#     """
#     This method create vm with timeout error
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     with pytest.raises(VMNotCreateTimeout) as err:
#         oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload', timeout=0)
#
#
# def test_wait_for_pod_initialized():
#     """
#     This method test wait for pod to be initialized
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     assert oc.wait_for_initialized(label='app=stressng_workload')
#
#
# def test_wait_for_pod_ready():
#     """
#     This method test wait for pod to be ready
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     oc.wait_for_initialized(label='app=stressng_workload')
#     assert oc.wait_for_ready(label='app=stressng_workload')
#
#
# # Stressng labels only: Need to fix it after updating labels in stressng vm
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_wait_for_vm_initialized():
#     """
#     This method test wait for vm to be initialized
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#     assert oc.wait_for_initialized(label='kubevirt.io=virt-launcher', label_uuid=False)
#
#
# # Stressng labels only: Need to fix it after updating labels in stressng vm
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_wait_for_vm_ready():
#     """
#     This method test wait for vm to be ready
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#     oc.wait_for_initialized(label='kubevirt.io=virt-launcher')
#     assert oc.wait_for_ready(label='kubevirt.io=virt-launcher', label_uuid=False)
#
#
# def test_wait_for_pod_completed():
#     """
#     This method test wait for pod to be completed
#     :return:
#     """
#     oc = OC()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     oc.wait_for_initialized(label='app=stressng_workload')
#     oc.wait_for_ready(label='app=stressng_workload')
#     assert oc.wait_for_completed(label='app=stressng_workload')
#
#
# # Stressng labels only: Need to fix it after updating labels in stressng vm
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_wait_for_vm_completed():
#     """
#     This method test wait for vm to be completed by verify ElasticSearch was populated with data
#     Must have running ElasticSearch server
#     :return:
#     """
#     if environment_variable['elasticsearch'] and environment_variable['elasticsearch_port']:
#         es = ESOperations(es_host=environment_variable['elasticsearch'],
#                           es_port=environment_variable['elasticsearch_port'])
#         oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#         oc.login()
#         oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#         oc.wait_for_initialized(label='kubevirt.io=virt-launcher', label_uuid=False)
#         oc.wait_for_ready(label='kubevirt.io=virt-launcher', label_uuid=False)
#         assert es.verify_es_data_uploaded(index='ripsaw-stressng-results', uuid=oc.get_long_uuid())
#     else:
#         print('There is no elastic search to verify VM completed status')
#
#
# def test_wait_for_pod_terminated():
#     """
#     This method test wait for pod to be terminated
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_pod_sync(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'), pod_name='stressng-workload')
#     oc.wait_for_initialized(label='app=stressng_workload')
#     oc.wait_for_ready(label='app=stressng_workload')
#     oc._delete_async(yaml=os.path.join(f'{templates_path}', 'stressng.yaml'))
#     assert oc.wait_for_pod_terminate(pod_name='stressng-workload')
#
#
# @pytest.mark.skip(reason="No Elastic Search support yet")
# def test_wait_for_vm_terminated():
#     """
#     This method test wait for vm to be terminated
#     :return:
#     """
#     oc = OC(kubeadmin_password=environment_variable['kubeadmin_password'])
#     oc.login()
#     oc.create_vm_sync(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'), vm_name='stressng-vm-benchmark-workload')
#     oc.wait_for_initialized(label='kubevirt.io=virt-launcher')
#     oc.wait_for_ready(label='kubevirt.io=virt-launcher')
#     oc._delete_async(yaml=os.path.join(f'{templates_path}', 'stressng_vm.yaml'))
#     oc.wait_for_vm_terminate(vm_name='stressng-vm-benchmark-workload')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
