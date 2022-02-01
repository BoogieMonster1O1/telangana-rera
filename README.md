# Telangana RERA Scraper ™

### Schema  
Output - Files consisting of 100 entries each (~41 files). Each file consists of a list of Root Objects
  
#### Root Object
|       Name       |            Description           |             Data type             |
|:----------------:|:--------------------------------:|:---------------------------------:|
|    projectName   |           Project Name           |               String              |
|   promoterName   |           Promoter Name          |               String              |
| lastModifiedDate |        Last Modified Date        |               String              |
|      pinCode     |             Pin Code             |               Number              |
| dateOfCompletion |    Proposed Date of Completion   |               String              |
|  buildingDetails |    List of Buildings' Details    | Array of Building Details Objects |
| professionalInfo | Project Professional Information |  Professional Information Object  |

#### Building Details Object
|    Name    |      Description      |         Data type         |
|:----------:|:---------------------:|:-------------------------:|
|    name    |  Name of the Building |           String          |
| floorInfos | Data stored per floor | List of Floor Data object |

#### Floor Data Object
|       Name       |            Description           | Data type |
|:----------------:|:--------------------------------:|:---------:|
|       srNo       |           Serial Number          |   Number  |
|      floorId     |             Floor ID             |   Number  |
|   mortgageArea   |           Mortgage Area          |  Boolean  |
|   apartmentType  |          Apartment Type          |   String  |
|   saleableArea   | Saleable Area (in square meters) |   Number  |
|    apartments    |       Number of Apartments       |   Number  |
| bookedApartments |    Number of Booked Apartments   |   Number  |

#### Professional Information Object
| Name |    Description    | Data type |
|:----:|:-----------------:|:---------:|
| name | Professional Name |   String  |
| type | Professional Type |   String  |
