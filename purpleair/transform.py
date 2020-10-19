from typing import List, Dict

def transform_record(record: Dict, column_to_property: Dict) -> Dict:
    """
    Takes a result Dict and returns a transformed Dict
    """
    transformed = {}
    for column, prop in column_to_property.items():
        transformed[column] = record.get(prop)
        # TODO: handle case when record doesn't have a value for the property
    return transformed


def transform_results(results: List, column_to_property: Dict) -> List:
    """
    Takes the results from the data download and a map of column names to result property names,
    and returns them as a transformed list
    """
    transformed_results = []
    for result in results:
        transformed = transform_record(result, column_to_property)
        transformed_results.append(transformed)
    return transformed_results