
from generate_schemas import run_schema_gen
from create_train_test_key_files import run_train_test_testkey_files_gen
from generate_inference_data import run_inference_request_data_gen


if __name__ == "__main__":
    run_schema_gen()
    run_train_test_testkey_files_gen()
    run_inference_request_data_gen()