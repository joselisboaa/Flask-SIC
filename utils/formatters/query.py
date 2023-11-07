

class QueryFormatter:
    """
        Esse método servirá para podermos transformar os dados numa
        Lista de Schema para podermos fazer o jsonify
    """
    def query_list_to_schema_list(self, query_result: list, schema):
        schematized_data_list = []

        for item in query_result:
            schematized_data = schema().dump(item)

            schematized_data_list.append(schematized_data)

        return schematized_data_list
