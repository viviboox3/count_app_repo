<<<<<<< HEAD
# monitoring_app
Project for CSCI-UA 480-005 Large Scale Web Applications Course
=======
# Metrix and Target_app
#### 
Metrix is an app that allows you to initialize Counters objects by specifying an app_name and a counter_name. You can then increment these counters when needed using increment() and increment_by() methods. Sample code can be found in testing.py. It also has a views.py file that displays these counters which are then scraped by a [monitoring app](https://github.com/aartibagul/monitoring_app) and displayed on a dashboard.

You must include  url(r'^metrix/', include('metrix.urls')) in the urls.py file of the project (in this case "test/urls.py").

#### testing.py
testing.py initializes two Counters from the metrix app and increments their values. As the name suggests, this is used for testing purposes.
>>>>>>> aecbde14bccb3f7b9899504cdb160f0775b7e9c8
