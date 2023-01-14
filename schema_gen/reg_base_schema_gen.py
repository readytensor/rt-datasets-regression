import numpy as np, pandas as pd
import os, sys
import yaml, json
import pprint
from pathlib import Path


version = "1.0"

model_category = "regression_base"


def get_schema_config():
    with open("config.yaml", "r") as f:
        try:
            config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as exc:
            print(exc)


def gen_reg_base_schemas(schema_cfg, root_path):

    model_category_config = schema_cfg["model_categories"][model_category]

    data_types = model_category_config["data_types"]
    field_use_types = model_category_config["field_use_types"]
    field_name_lbl = model_category_config["schemaFields"]["fieldName"]
    data_type_lbl = model_category_config["schemaFields"]["dataType"]
    use_type_lbl = model_category_config["schemaFields"]["fieldUseType"]

    datasets = model_category_config["datasets"]

    for dataset in datasets:

        print(f"Generating schema for model_cat: {model_category}  dataset: {dataset}")

        # initiate the schema dict
        schema_dict = {}
        schema_dict["problemCategory"] = model_category
        schema_dict["version"] = version
        schema_dict["inputDatasets"] = {
            "regressionBaseMainInput": {
                "idField": "",
                "targetField": "",
                "predictorFields": [],
            }
        }

        schema_dirpath = os.path.join(root_path, "datasets", dataset, "schema_cfg")
        input_fpath = os.path.join(schema_dirpath, datasets[dataset]["fname"])
        schema_params = pd.read_csv(input_fpath)
        fname_wo_ext = Path(datasets[dataset]["fname"]).stem

        output_fpath = os.path.join(
            root_path,
            "datasets",
            dataset,
            "processed",
            f"{dataset}_schema.json",
        )

        input_dict = schema_dict["inputDatasets"]["regressionBaseMainInput"]

        id_attr = None
        target_attr = None

        # iterate through the fields in the input file
        for _, row in schema_params.iterrows():

            if row[use_type_lbl] == field_use_types["id"]:
                if id_attr is not None:
                    raise Exception(
                        f"Error: Only 1 id row is permissible. Can't set {row['field_name_lbl']}"
                    )
                id_attr = row[field_name_lbl]
                input_dict["idField"] = id_attr

            elif row[use_type_lbl] == field_use_types["target"]:
                if target_attr is not None:
                    raise Exception(
                        f"Error: Only 1 target attr is permissible. Can't set {row['field_name_lbl']}"
                    )
                target_attr = row[field_name_lbl]
                input_dict["targetField"] = target_attr

            elif row[use_type_lbl] == field_use_types["input"]:
                attribute = {}
                attribute["fieldName"] = row[field_name_lbl]

                if (
                    row[data_type_lbl] == data_types["categorical"]
                    or row[data_type_lbl] == data_types["string"]
                    or row[data_type_lbl] == data_types["numeric"]
                ):

                    attribute["dataType"] = row[data_type_lbl]
                    input_dict["predictorFields"].append(attribute)
                else:
                    raise Exception(f"What data type is this: {row[data_type_lbl]}")

            elif row[use_type_lbl] == field_use_types["info"]:
                # noop
                pass

            else:
                raise Exception(f"What use type is this: {row[use_type_lbl]}")

        # pprint.pprint(schema_dict)
        with open(output_fpath, "w") as f:
            json.dump(schema_dict, f, indent=2)


if __name__ == "__main__":

    root_path = f"./../"

    model_categories = [
        "regression_base",
    ]

    schema_cfg = get_schema_config()

    gen_reg_base_schemas(schema_cfg, root_path)
