import sys

# ESTOS BINS SON LOS DE LA CLASE, TENEMOS QUE CREAR LOS NUESTROS (NO SE COMO)
bins = {"loan_amnt": [{"label": "(-inf,1000.0)", "max": 1000.0}, {"label": "(1000.0,9500.0)", "max": 9500.0},
                      {"label": "(9500.0,18000.0)", "max": 18000.0}, {"label": "(18000.0,inf)", "max": sys.maxsize}, ],

        "funded_amnt": [{"label": "(-inf,1000.0)", "max": 1000.0}, {"label": "(1000.0,5857.0)", "max": 5857.0},
                        {"label": "(5857.0,10714.0)", "max": 10714.0}, {"label": "(10714.0,15571.0)", "max": 15571.0},
                        {"label": "(15571.0,20429.0)", "max": 20429.0}, {"label": "(20429.0,25286.0)", "max": 25286.0},
                        {"label": "(25286.0,inf)", "max": sys.maxsize}, ],

        "int_rate": [{"label": "(-inf,6.0)", "max": 6.0}, {"label": "(6.0,9.0)", "max": 9.0},
                     {"label": "(9.0,12.0)", "max": 12.0}, {"label": "(12.0,15.0)", "max": 15.0},
                     {"label": "(15.0,17.0)", "max": 17.0}, {"label": "(17.0,20.0)", "max": 20.0},
                     {"label": "(20.0,inf)", "max": sys.maxsize}, ],

        "installment": [{"label": "(-inf,23.0)", "max": 23.0}, {"label": "(23.0,254.0)", "max": 254.0},
                        {"label": "(254.0,486.0)", "max": 486.0}, {"label": "(486.0,717.0)", "max": 717.0},
                        {"label": "(717.0,948.0)", "max": 948.0}, {"label": "(948.0,inf)", "max": sys.maxsize}, ],

        "annual_inc": [{"label": "(-inf,7000.0)", "max": 7000.0}, {"label": "(7000.0,178500.0)", "max": 178500.0},
                       {"label": "(178500.0,350000.0)", "max": 350000.0},
                       {"label": "(350000.0,521500.0)", "max": 521500.0},
                       {"label": "(521500.0,693000.0)", "max": 693000.0},
                       {"label": "(693000.0,inf)", "max": sys.maxsize}, ],

        "dti": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,7.0)", "max": 7.0},
                {"label": "(7.0,13.0)", "max": 13.0}, {"label": "(13.0,20.0)", "max": 20.0},
                {"label": "(20.0,27.0)", "max": 27.0}, {"label": "(27.0,inf)", "max": sys.maxsize}, ],

        "revol_bal": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,640176.0)", "max": 640176.0},
                      {"label": "(640176.0,1280352.0)", "max": 1280352.0},
                      {"label": "(1280352.0,inf)", "max": sys.maxsize}, ],

        "revol_util": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,37.0)", "max": 37.0},
                       {"label": "(37.0,74.0)", "max": 74.0}, {"label": "(74.0,inf)", "max": sys.maxsize}, ],

        "total_acc": [{"label": "(-inf,2.0)", "max": 2.0}, {"label": "(2.0,23.0)", "max": 23.0},
                      {"label": "(23.0,44.0)", "max": 44.0}, {"label": "(44.0,65.0)", "max": 65.0},
                      {"label": "(65.0,87.0)", "max": 87.0}, {"label": "(87.0,108.0)", "max": 108.0},
                      {"label": "(108.0,inf)", "max": sys.maxsize}, ],

        "out_prncp": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,8040.0)", "max": 8040.0},
                      {"label": "(8040.0,16080.0)", "max": 16080.0}, {"label": "(16080.0,inf)", "max": sys.maxsize}, ],

        "total_pymnt": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,13786.0)", "max": 13786.0},
                        {"label": "(13786.0,27573.0)", "max": 27573.0},
                        {"label": "(27573.0,inf)", "max": sys.maxsize}, ],

        "total_rec_prncp": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,5833.0)", "max": 5833.0},
                            {"label": "(5833.0,11667.0)", "max": 11667.0},
                            {"label": "(11667.0,17500.0)", "max": 17500.0},
                            {"label": "(17500.0,23333.0)", "max": 23333.0},
                            {"label": "(23333.0,inf)", "max": sys.maxsize}, ],

        "total_rec_int": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,3069.0)", "max": 3069.0},
                          {"label": "(3069.0,6139.0)", "max": 6139.0}, {"label": "(6139.0,9208.0)", "max": 9208.0},
                          {"label": "(9208.0,12277.0)", "max": 12277.0}, {"label": "(12277.0,15346.0)", "max": 15346.0},
                          {"label": "(15346.0,inf)", "max": sys.maxsize}, ],

        "total_rec_late_fee": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,51.0)", "max": 51.0},
                               {"label": "(51.0,102.0)", "max": 102.0}, {"label": "(102.0,154.0)", "max": 154.0},
                               {"label": "(154.0,205.0)", "max": 205.0}, {"label": "(205.0,256.0)", "max": 256.0},
                               {"label": "(256.0,inf)", "max": sys.maxsize}, ],

        "recoveries": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,4789.0)", "max": 4789.0},
                       {"label": "(4789.0,9577.0)", "max": 9577.0}, {"label": "(9577.0,14366.0)", "max": 14366.0},
                       {"label": "(14366.0,19154.0)", "max": 19154.0}, {"label": "(19154.0,23943.0)", "max": 23943.0},
                       {"label": "(23943.0,inf)", "max": sys.maxsize}, ],

        "collection_recovery_fee": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,813.0)", "max": 813.0},
                                    {"label": "(813.0,1627.0)", "max": 1627.0},
                                    {"label": "(1627.0,2440.0)", "max": 2440.0},
                                    {"label": "(2440.0,3254.0)", "max": 3254.0},
                                    {"label": "(3254.0,4067.0)", "max": 4067.0},
                                    {"label": "(4067.0,inf)", "max": sys.maxsize}, ],

        "last_pymnt_amnt": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,6007.0)", "max": 6007.0},
                            {"label": "(6007.0,12015.0)", "max": 12015.0},
                            {"label": "(12015.0,18022.0)", "max": 18022.0},
                            {"label": "(18022.0,24029.0)", "max": 24029.0},
                            {"label": "(24029.0,inf)", "max": sys.maxsize}, ],

        "tot_coll_amt": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,15968.0)", "max": 15968.0},
                         {"label": "(15968.0,31935.0)", "max": 31935.0}, {"label": "(31935.0,47903.0)", "max": 47903.0},
                         {"label": "(47903.0,63871.0)", "max": 63871.0},
                         {"label": "(63871.0,inf)", "max": sys.maxsize}, ],

        "tot_cur_bal": [{"label": "(-inf,0.0)", "max": 0.0}, {"label": "(0.0,960199.0)", "max": 960199.0},
                        {"label": "(960199.0,1920398.0)", "max": 1920398.0},
                        {"label": "(1920398.0,inf)", "max": sys.maxsize}, ],

        "total_rev_hi_lim": [{"label": "(-inf,100.0)", "max": 100.0}, {"label": "(100.0,1428657.0)", "max": 1428657.0},
                             {"label": "(1428657.0,2857214.0)", "max": 2857214.0},
                             {"label": "(2857214.0,4285771.0)", "max": 4285771.0},
                             {"label": "(4285771.0,5714328.0)", "max": 5714328.0},
                             {"label": "(5714328.0,7142885.0)", "max": 7142885.0},
                             {"label": "(7142885.0,inf)", "max": sys.maxsize}, ]
}
