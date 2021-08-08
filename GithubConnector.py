import requests
import sys

class GithubConnector:

   def __init__(self):
      self.github_url_separator = "/"
      self.github_api_url = "https://api.github.com/repos/"
      self.github_username = "henriquepgomide"
      self.github_repository = "caRtola"
      self.github_contents_url = self.github_api_url + self.github_username + self.github_url_separator \
         + self.github_repository + self.github_url_separator + "contents" + self.github_url_separator
      # github_contents_url fica igual a: https://api.github.com/repos/henriquepgomide/caRtola/contents/data
      self.github_data_url = self.github_contents_url + "data" + self.github_url_separator

   def GetCsvRoundFilesUrlByYear(self, years):
      dict_of_files = {}
      # Pega cada arquivo CSV do repositório 
      for year in years:
         response = requests.get(self.github_data_url + str(year))
         json_response = response.json()
         
         i = 0
         for json_file in json_response:
            # Pega os arquivos CSV de Rodadas daquele ano
            if "rodada-" in json_file["name"] and ".csv" in json_file["name"]:
               file_name = json_file["name"]
               download_url = json_file["download_url"]
               print(download_url)
               dict_of_files[file_name] = download_url

      return dict_of_files