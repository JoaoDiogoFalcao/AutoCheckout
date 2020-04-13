# CPS-IoT Week Competition
Welcome to AiFi's CPS-IoT Autocheckout Competition. This document details the competition and will help you get started.

## Overview
This repository will help you get started with examples on how to use the Public Datasets available at http://aifi.io/research under Sample Data.

To start please download the data labelled as: "Simple Example" without depth (For your first example).

During the competition you will need a competitor token that will distinguish your submission from all other competitors. However you do
not need this token for your local testing environment.

## Sample Data

In order for the example to work properly download the data into `data/downloads`.

### Simple Example
Download Videos [Here](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-01/cps-test-videos.gz) (17.1MB)

Download Data without Depth Images [Here](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-01/cps-test-01-nodepth.archive) (239MB)

Download Data with Depth Images [Here](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-01/cps-test-01-all.archive) (2.0GB)

### Multiple People Dataset

Test Case | Data w/ Depth | Camera Calibration
---|---|---
Simple Case | [Donwload](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-01/cps-test-videos.gz?authuser=1) |  [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-01/cps-test-01-all.archive?authuser=1) | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-01/cps-test-01-nodepth.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_1-1_camera_calibration.json)
| Test 2 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-02/cps-test-02-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 3 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-03/cps-test-03-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 4 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-04/cps-test-04-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 5 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-05/cps-test-05-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 6 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-06/cps-test-06-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 7 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-07/cps-test-07-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 8 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-08/cps-test-08-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 9 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-09/cps-test-09-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 10 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-10/cps-test-10-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 11 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-11/cps-test-11-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 12 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-12/cps-test-12-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 13 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-13/cps-test-13-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 14 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-14/cps-test-14-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 15 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-15/cps-test-15-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 16 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-16/cps-test-16-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 17 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-17/cps-test-17-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 18 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-18/cps-test-18-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 19 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-19/cps-test-19-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 20 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-20/cps-test-20-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 21 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-21/cps-test-21-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 22 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-22/cps-test-22-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 23 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-23/cps-test-23-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)
| Test 24 | [Download](https://storage.cloud.google.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/cps-test-24/cps-test-24-all.archive?authuser=1) | [Download](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/calibration/cps_week_test_cases_2-24_camera_calibration.json)

### Product Images

You can find high-quality images of the products in the store [here](https://storage.googleapis.com/aifi-public-data/AiFi%20Nanostore%20AutoCheckout%20Competition%20-%20CPS-IoT%20Week%202020/training/products_18.zip). Feel free to use them to train product detection/classification models.  
Note: For now, images from only 18 products are available, we'll update the readme as soon as other products become available.

Products:

UPC/EAN | Link
--- | ---
012000028458 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000028458.zip)
022000135377 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/022000135377.zip)
028400337298 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400337298.zip)
044000052317 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/044000052317.zip)
04963406     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/04963406.zip)
076406022502 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406022502.zip)
084114033000 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/084114033000.zip)
611269357011 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269357011.zip)
786162002976 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/786162002976.zip)
835144008915 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144008915.zip)
858176002058 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858176002058.zip)
012000028472 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000028472.zip)
024100114238 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/024100114238.zip)
028400449373 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400449373.zip)
048500201466 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/048500201466.zip)
04965802     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/04965802.zip)
076406023103 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406023103.zip)
084114033338 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/084114033338.zip)
611269402186 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269402186.zip)
786162070005 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/786162070005.zip)
835144008977 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144008977.zip)
858176002065 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858176002065.zip)
012000043000 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000043000.zip)
024100191345 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/024100191345.zip)
028400589895 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400589895.zip)
049000014235 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000014235.zip)
04997704     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/04997704.zip)
077208007629 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/077208007629.zip)
084114115881 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/084114115881.zip)
611269716467 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269716467.zip)
786162080004 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/786162080004.zip)
835144008984 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144008984.zip)
858176002508 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858176002508.zip)
012000110443 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000110443.zip)
024100203628 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/024100203628.zip)
028400629591 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400629591.zip)
049000014266 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000014266.zip)
052000042283 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000042283.zip)
078000082166 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078000082166.zip)
084114125514 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/084114125514.zip)
611269818994 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269818994.zip)
786162150004 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/786162150004.zip)
835144009035 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144009035.zip)
858176002522 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858176002522.zip)
012000110467 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000110467.zip)
024100204113 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/024100204113.zip)
028400642033 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400642033.zip)
049000024685 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000024685.zip)
052000043167 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000043167.zip)
078000146455 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078000146455.zip)
087684001073 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/087684001073.zip)
613008715267 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/613008715267.zip)
786162338006 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/786162338006.zip)
835144009042 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144009042.zip)
858369006177 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858369006177.zip)
012000151163 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000151163.zip)
024100315345 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/024100315345.zip)
028400642255 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400642255.zip)
049000024692 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000024692.zip)
052000102390 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000102390.zip)
078000152456 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078000152456.zip)
090478410012 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/090478410012.zip)
613008723422 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/613008723422.zip)
787692870011 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/787692870011.zip)
835144009059 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144009059.zip)
858369006191 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858369006191.zip)
012000162152 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000162152.zip)
026200471587 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/026200471587.zip)
028400644327 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400644327.zip)
049000024708 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000024708.zip)
052000207149 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000207149.zip)
078000153453 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078000153453.zip)
090478410029 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/090478410029.zip)
613008743734 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/613008743734.zip)
810002650017 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/810002650017.zip)
835144009066 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144009066.zip)
858369006207 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/858369006207.zip)
012000170799 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000170799.zip)
026200471594 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/026200471594.zip)
028400644747 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400644747.zip)
049000028904 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000028904.zip)
052000207224 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000207224.zip)
07831504     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/07831504.zip)
090478410036 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/090478410036.zip)
613008744090 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/613008744090.zip)
811620020756 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/811620020756.zip)
835144009073 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144009073.zip)
872181000069 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/872181000069.zip)
012000180361 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000180361.zip)
028400000666 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400000666.zip)
028400645249 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400645249.zip)
049000028911 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000028911.zip)
052000207309 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000207309.zip)
078742025018 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742025018.zip)
095188955914 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/095188955914.zip)
613008744120 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/613008744120.zip)
811955011016 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/811955011016.zip)
835144009080 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144009080.zip)
888903201102 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/888903201102.zip)
012000181290 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000181290.zip)
028400001342 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400001342.zip)
034000996629 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/034000996629.zip)
049000028928 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000028928.zip)
052000326734 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/052000326734.zip)
078742089621 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742089621.zip)
095188995910 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/095188995910.zip)
632432737775 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/632432737775.zip)
812186020426 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/812186020426.zip)
836093010523 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/836093010523.zip)
888903201119 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/888903201119.zip)
012000286209 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000286209.zip)
028400001748 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400001748.zip)
038000138416 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/038000138416.zip)
049000030730 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000030730.zip)
059654510014 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/059654510014.zip)
078742125718 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742125718.zip)
096619506897 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/096619506897.zip)
632565000029 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/632565000029.zip)
812475012262 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/812475012262.zip)
836093011025 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/836093011025.zip)
888903201188 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/888903201188.zip)
012000809941 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000809941.zip)
028400002912 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400002912.zip)
038000138430 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/038000138430.zip)
049000030754 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000030754.zip)
070462098617 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/070462098617.zip)
078742125763 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742125763.zip)
4000177605004 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/4000177605004.zip)
632565000036 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/632565000036.zip)
813694023428 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/813694023428.zip)
836093011056 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/836093011056.zip)
889497852367 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/889497852367.zip)
012000809965 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/012000809965.zip)
028400014236 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400014236.zip)
038000138577 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/038000138577.zip)
049000072372 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000072372.zip)
070847012474 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/070847012474.zip)
078742125770 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742125770.zip)
54491472     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/54491472.zip)
634418523488 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/634418523488.zip)
813694023466 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/813694023466.zip)
836093011070 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/836093011070.zip)
891760002508 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/891760002508.zip)
01201303     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/01201303.zip)
028400034005 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400034005.zip)
038000183713 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/038000183713.zip)
049000072389 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000072389.zip)
071063437072 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/071063437072.zip)
078742125794 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742125794.zip)
610764000316 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764000316.zip)
634418523501 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/634418523501.zip)
813694024258 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/813694024258.zip)
850251004001 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/850251004001.zip)
891760002560 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/891760002560.zip)
01205008     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/01205008.zip)
028400040037 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400040037.zip)
040000513056 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/040000513056.zip)
049000072396 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000072396.zip)
071063437089 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/071063437089.zip)
078742148038 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742148038.zip)
610764251299 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764251299.zip)
681131780957 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/681131780957.zip)
818094000017 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818094000017.zip)
850251004087 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/850251004087.zip)
898999010007 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/898999010007.zip)
01208500     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/01208500.zip)
028400040112 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400040112.zip)
041364087320 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/041364087320.zip)
049000075304 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000075304.zip)
071063437553 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/071063437553.zip)
078742162027 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078742162027.zip)
610764826114 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764826114.zip)
681131780964 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/681131780964.zip)
818094000024 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818094000024.zip)
851861006102 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/851861006102.zip)
898999010144 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/898999010144.zip)
01215908     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/01215908.zip)
028400047944 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400047944.zip)
041419420058 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/041419420058.zip)
049000075311 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000075311.zip)
071146002524 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/071146002524.zip)
078907420108 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078907420108.zip)
610764826176 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764826176.zip)
722430110165 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/722430110165.zip)
818094000703 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818094000703.zip)
852311004013 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004013.zip)
898999010656 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/898999010656.zip)
01264904     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/01264904.zip)
028400055116 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400055116.zip)
041419420065 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/041419420065.zip)
049000079333 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079333.zip)
071146002555 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/071146002555.zip)
078907440489 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078907440489.zip)
610764863430 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764863430.zip)
728229014799 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/728229014799.zip)
818094002240 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818094002240.zip)
852311004020 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004020.zip)
898999010670 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/898999010670.zip)
014100075233 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/014100075233.zip)
028400055154 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400055154.zip)
042238323643 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/042238323643.zip)
049000079357 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079357.zip)
073360237515 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/073360237515.zip)
078907916335 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078907916335.zip)
610764863638 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764863638.zip)
742365004209 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/742365004209.zip)
818094002905 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818094002905.zip)
852311004037 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004037.zip)
898999010717 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/898999010717.zip)
016000126060 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016000126060.zip)
028400064088 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400064088.zip)
042743190884 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/042743190884.zip)
049000079364 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079364.zip)
076183003114 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076183003114.zip)
078907916342 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/078907916342.zip)
610764863812 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/610764863812.zip)
757528008680 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/757528008680.zip)
818780011938 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818780011938.zip)
852311004273 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004273.zip)
90162800     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/90162800.zip)
016000126077 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016000126077.zip)
028400090148 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400090148.zip)
042743191195 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/042743191195.zip)
049000079371 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079371.zip)
076183003282 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076183003282.zip)
079200168490 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/079200168490.zip)
611269133448 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269133448.zip)
757528008697 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/757528008697.zip)
818780014229 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818780014229.zip)
852311004518 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004518.zip)
90162909     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/90162909.zip)
016000160101 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016000160101.zip)
028400090858 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400090858.zip)
043000028254 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/043000028254.zip)
049000079388 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079388.zip)
076406021505 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406021505.zip)
082592727152 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/082592727152.zip)
611269163452 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269163452.zip)
7640131280211 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/7640131280211.zip)
818780014243 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/818780014243.zip)
852311004525 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004525.zip)
016000166196 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016000166196.zip)
028400090896 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400090896.zip)
043000953709 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/043000953709.zip)
049000079395 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079395.zip)
076406021604 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406021604.zip)
083791126050 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/083791126050.zip)
611269206432 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269206432.zip)
7640143481699 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/7640143481699.zip)
829515307172 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/829515307172.zip)
852311004532 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852311004532.zip)
016000502789 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016000502789.zip)
028400091510 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400091510.zip)
043000953730 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/043000953730.zip)
049000079418 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/049000079418.zip)
076406021703 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406021703.zip)
083791126074 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/083791126074.zip)
611269212457 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269212457.zip)
7640146940315 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/7640146940315.zip)
835143001795 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835143001795.zip)
852909003527 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852909003527.zip)
016571940331 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016571940331.zip)
028400159388 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400159388.zip)
044000003067 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/044000003067.zip)
04904403     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/04904403.zip)
076406021802 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406021802.zip)
083900005757 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/083900005757.zip)
611269226126 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269226126.zip)
7640146941626 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/7640146941626.zip)
835143013156 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835143013156.zip)
852909003541 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/852909003541.zip)
016571950293 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016571950293.zip)
028400199148 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400199148.zip)
044000006778 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/044000006778.zip)
04905004     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/04905004.zip)
076406022304 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406022304.zip)
083900005771 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/083900005771.zip)
611269235685 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269235685.zip)
7640146941862 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/7640146941862.zip)
835144008687 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144008687.zip)
853247003026 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/853247003026.zip)
016571953386 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/016571953386.zip)
028400207430 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/028400207430.zip)
044000006792 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/044000006792.zip)
04913207     | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/04913207.zip)
076406022403 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/076406022403.zip)
084114032607 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/084114032607.zip)
611269321210 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/611269321210.zip)
781138710183 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/781138710183.zip)
835144008762 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/835144008762.zip)
853311003600 | [Download](https://storage.cloud.google.com/aifi-public-data/sku-only/photobox/853311003600.zip)



## Getting Started

### Obtain a competitor token
After submitting your abstract describing your approach you will receive a competitor token.
Do not share your token with anyone outside your team. It will be used to uniquely identify you, access test cases, and to submit your results.
Set it to an env variable for later use.
```
export AIFI_CPSWEEK_COMP__TOKEN=<your-token>
```

### Dependencies
Before you begin, you will need to setup a few dependencies:
- *`docker`*: [Install Docker](https://docs.docker.com/install/)
- *`docker-compose`*: [Install `docker-compose`](https://docs.docker.com/compose/install/)

### Clone
This repo provides everything you need to get started. Begin by cloning this repo.
```
# Clone the repo
git clone https://github.com/JoaoDiogoFalcao/AutoCheckout.git
cd AutoCheckout/
```

### Test
After you have cloned the repo, you can execute the solution against an example and print the results with the following command.
```
AIFI_CPSWEEK_COMP__COMMAND=cps-test-01 docker-compose up --build
```

### Submit
You will be able to submit your solution after you have submitted your abstract and received a competitor token.

## FAQ
Before contacting AiFi, check the frequently asked questions below.

### I saw this error:
- `PermissionError: [Errno 13] Permission denied:`
  - The files backing the mongodb are owned by a user you do not have permissions to access. Run the `docker-compose` with `sudo`

### Can I add my own dependencies?
Yes. Just add them to `requirements.txt`.

### Can I use a GPU acceleration?
Yes. See Docker's guide on leveraging GPU in docker containers.

### The docker compose never returns!
You can send a SIGTERM to the program while it's in the foreground with ctrl-C or you can run the `docker-compose` command with the option `--abort-on-container-exit`

### Sensor Data Questions
####  What is the sample rate?
The sensor data is sampled at 60Hz. Each message contains a batch of 12 samples.

####  What is the noise level?
The noise level varies highly from testcase to testcase and from shelf to shelf due to environmental factors such as nearby vibrations and electrical noise.

#### What is the max weight?
The sensors are rated for 20kg per plate.

#### Do I need to account for sensor nonlinearity?
No. The nonlinearity error is orders of magnitude below the baseline noise from the environment.

#### Are the absolute weight values reliable?
No. The absolute weight measured by the sensors is not zeroed and may drift over long periods of time (hours or days). Relatively changes, however, are reliable.
