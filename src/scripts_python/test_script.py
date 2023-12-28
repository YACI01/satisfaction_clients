import unittest
from elasticsearch import Elasticsearch
import csv

class TestBusinessQueries(unittest.TestCase):
    def setUp(self):
        # Initialiser une instance d'Elasticsearch pour les tests
        self.es = Elasticsearch(hosts="http://localhost:9200")
        self.index_name = "review3"  # Nom de l'index

    def test_index_exists(self):
        # Vérifier si l'index spécifié dans le script existe
        index_exists = self.es.indices.exists(index=self.index_name)
        self.assertTrue(index_exists)

    def test_data_inserted(self):
        # Vérifier si des données ont été insérées dans l'index
        response = self.es.search(index=self.index_name)
        total_hits = response["hits"]["total"]["value"]
        self.assertGreater(total_hits, 0)

    def test_mapping_correct(self):
        # Vérifier si le mapping de l'index correspond à ce qui est attendu
        mapping = {
            "mappings": {
                "properties": {
                    "@timestamp": {"type": "date"},
                    "Company": {"type": "keyword"},
                    "Customer": {"type": "keyword"},
                    "Date_experience": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                    "Date_reply": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                    "Date_review": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
                    "Experience": {"type": "keyword"},
                    "Language": {"type": "keyword"},
                    "Number_review": {"type": "long"},
                    "Rating": {"type": "long"},
                    "Reply": {"type": "keyword"},
                    "Status": {"type": "keyword"},
                    "Title": {"type": "keyword"},
                    "column1": {"type": "long"},
                    "document_id": {"type": "keyword"}
                }
            }
        }

        # Récupérez le mappage réel de l'index
        actual_mapping = self.es.indices.get_mapping(index=self.index_name)

        # Extrait le mappage de "properties" du mappage réel
        actual_mapping_properties = actual_mapping[self.index_name]["mappings"]["properties"]

        # Comparez le mappage attendu aux propriétés du mappage réel
        self.assertEqual(mapping["mappings"]["properties"], actual_mapping_properties)
        
        actual_mapping = self.es.indices.get_mapping(index=self.index_name)
        self.assertEqual(mapping, actual_mapping[self.index_name]["mappings"])

if __name__ == '__main__':
    unittest.main()
