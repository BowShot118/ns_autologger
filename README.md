# ns_autologger
An autologger script for NationStates.
## Requirements:
- Python 3.13
- Requests Library: https://pypi.org/project/requests/
## Installation
- Download and install Python 3.13 and the requests library
- Download the repository (Code -> Download ZIP)
- Update the script to include a UserAgent. This should identify you, e.g. your nation name or email address
## Running
- Fill out the "nationPasswords.csv" file with the nations you wish for the autologger to log into using the "nation,password" format and save
- Run the program. It may return up to two lists if there are issues logging into nations:
  - cteList.csv if a nation in your list does not exist
  - failedList.csv if any other issue was encountered with attempting to log into the nation
