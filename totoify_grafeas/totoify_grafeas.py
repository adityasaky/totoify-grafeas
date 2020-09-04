from in_toto.models.link import Link
from in_toto.models.metadata import Metablock


class GrafeasLink:
  command = []
  environment = {}
  byproducts = {}
  materials = []
  products = []

  def __init__(self, link_materials, link_products, link_command,
      link_byproducts, link_environment):

    for resource_uri, hash_object in link_materials.items():
      self.materials.append({
          "resource_uri": resource_uri,
          "hashes": {
            "sha256": hash_object["sha256"]
          }
        }
      )

    for resource_uri, hash_object in link_products.items():
      self.products.append({
          "resource_uri": resource_uri,
          "hashes": {
            "sha256": hash_object["sha256"]
          }
        }
      )
    self.command = link_command
    
    for key, value in link_byproducts.items():
      self.link_byproducts['custom_values'][key] = value

    for key, value in link_environment.items():
      self.link_environment['custom_values'][key] = value



class GrafeasInTotoOccurrence:
  signatures = []
  signed = None

  def __init__(self, in_toto_link):
    self.signed = GrafeasLink(in_toto_link["signed"]["materials"],
                              in_toto_link["signed"]["products"],
                              in_toto_link["signed"]["command"],
                              in_toto_link["signed"]["byproducts"],
                              in_toto_link["signed"]["environment"])

    self.signatures = in_toto_link["signatures"]


def create_grafeas_occurrence_from_in_toto_link(in_toto_link):
  return GrafeasInTotoOccurrence(in_toto_link)


def create_in_toto_link_from_grafeas_occurrence(grafeas_occurrence, step_name):
  materials = {}
  products = {}
  command = []
  byproducts = {}
  environment = {}

  for item in grafeas_occurrence.signed.materials:
    materials[item["resource_uri"]] = item["hashes"]

  for item in grafeas_occurrence.signed.products:
    products[item["resource_uri"]] = item["hashes"]

  command = grafeas_occurrence.signed.command

  for key, value in byproducts.items():
    if key == "custom_values":
      continue
    byproducts[key] = value

  for key, value in byproducts["custom_values"].items():
    byproducts[key] = value

  for key, value in environment.items():
    if key == "custom_values":
      continue
    environment[key] = value

  for key, value in environment["custom_values"].items():
    environment[key] = value
  
  in_toto_link =  Link(name=step_name, materials=materials, products=products, byproducts=byproducts, command=command, environment=environment)

  return Metablock(signed=in_toto_link, signatures=grafeas_occurrence.signatures)
