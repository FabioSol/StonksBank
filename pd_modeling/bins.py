import sys

bins = {"loan_amnt": [{"label": "(-inf,1000.0)", "max": 1000.0}, {"label": "(1000.0,9500.0)", "max": 9500.0},
                      {"label": "(9500.0,18000.0)", "max": 18000.0}, {"label": "(18000.0,inf)", "max": sys.maxsize}, ],

        "funded_amnt": [{"label": "(-inf,1000.0)", "max": 1000.0}, {"label": "(1000.0,5857.0)", "max": 5857.0},
                        {"label": "(5857.0,10714.0)", "max": 10714.0}, {"label": "(10714.0,15571.0)", "max": 15571.0},
                        {"label": "(15571.0,20429.0)", "max": 20429.0}, {"label": "(20429.0,25286.0)", "max": 25286.0},
                        {"label": "(25286.0,inf)", "max": sys.maxsize}, ],

        "int_rate": [{"label": "(-inf,9.0)", "max": 9.0},
                     {"label": "(9.0,12.0)", "max": 12.0},
                     {"label": "(12.0,17.0)", "max": 17.0}, {"label": "(17.0,20.0)", "max": 20.0},
                     {"label": "(20.0,inf)", "max": sys.maxsize}, ],

        "installment": [{"label": "(-inf,23.0)", "max": 23.0}, {"label": "(23.0,254.0)", "max": 254.0},
                        {"label": "(254.0,486.0)", "max": 486.0}, {"label": "(486.0,717.0)", "max": 717.0},
                        {"label": "(717.0,948.0)", "max": 948.0}, {"label": "(948.0,inf)", "max": sys.maxsize}, ],

        "annual_inc": [{"label": "(-inf,7000.0)", "max": 7000.0}, {"label": "(7000.0,178500.0)", "max": 178500.0},
                       {"label": "(178500.0,350000.0)", "max": 350000.0},
                       {"label": "(350000.0,521500.0)", "max": 521500.0},
                       {"label": "(521500.0,693000.0)", "max": 693000.0},
                       {"label": "(693000.0,inf)", "max": sys.maxsize}, ],

        "dti": [{"label": "(-inf,3.0)", "max": 3.0}, {"label": "(3.0,7.0)", "max": 7.0},
                {"label": "(7.0,13.0)", "max": 13.0}, {"label": "(13.0,20.0)", "max": 20.0},
                {"label": "(20.0,27.0)", "max": 27.0}, {"label": "(27.0,inf)", "max": sys.maxsize}, ],

        "revol_bal": [{"label": "(-inf,10000.0)", "max": 10000.0}, {"label": "(10000.0,500000.0)", "max": 500000.0},
                      {"label": "(500000.0,700000.0)", "max": 700000.0},
                      {"label": "(700000.0,inf)", "max": sys.maxsize}, ],

        "revol_util": [{"label": "(-inf,15.0)", "max": 15.0}, {"label": "(15.0,37.0)", "max": 37.0},
                       {"label": "(37.0,74.0)", "max": 74.0}, {"label": "(74.0,inf)", "max": sys.maxsize}, ],

        "total_acc": [{"label": "(-inf,12.0)", "max": 12.0}, {"label": "(12.0,23.0)", "max": 23.0},
                      {"label": "(23.0,44.0)", "max": 44.0}, {"label": "(44.0,65.0)", "max": 65.0},
                      {"label": "(65.0,87.0)", "max": 87.0}, {"label": "(87.0,108.0)", "max": 108.0},
                      {"label": "(108.0,inf)", "max": sys.maxsize}, ],

        "out_prncp": [{"label": "(-inf,2000.0)", "max": 2000.0}, {"label": "(2000.0,8040.0)", "max": 8040.0},
                      {"label": "(8040.0,inf)", "max": sys.maxsize}, ],

        "total_pymnt": [{"label": "(-inf,7000)", "max": 7000}, {"label": "(7000.0,25000.0)", "max": 25000.0},
                        {"label": "(25000.0,inf)", "max": sys.maxsize}, ],

        "total_rec_prncp": [{"label": "(-inf,5833.0)", "max": 5833.0},
                            {"label": "(5833.0,11667.0)", "max": 11667.0},
                            {"label": "(11667.0,17500.0)", "max": 17500.0},
                            {"label": "(17500.0,22000.0)", "max": 22000.0},
                            {"label": "(22000.0,inf)", "max": sys.maxsize}, ],

        "total_rec_int": [{"label": "(-inf,1000)", "max": 1000}, {"label": "(1000.0,3069.0)", "max": 3069.0},
                          {"label": "(3069.0,6139.0)", "max": 6139.0}, {"label": "(6139.0,9208.0)", "max": 9208.0},
                          {"label": "(9208.0,12277.0)", "max": 12277.0}, {"label": "(12277.0,14000.0)", "max": 14000.0},
                          {"label": "(14000.0,inf)", "max": sys.maxsize}, ],

        "total_rec_late_fee": [{"label": "(-inf,2.0)", "max": 2}, {"label": "(2.0,40.0)", "max": 40.0},
                               {"label": "(40.0,60.0)", "max": 60.0},
                               {"label": "(60.0,90.0)", "max": 90.0},
                               {"label": "(90.0,inf)", "max": sys.maxsize}, ],


        "last_pymnt_amnt": [{"label": "(-inf,6007.0)", "max": 6007.0},
                            {"label": "(6007.0,12015.0)", "max": 12015.0},
                            {"label": "(12015.0,18022.0)", "max": 18022.0},
                            {"label": "(18022.0,23000.0)", "max": 23000.0},
                            {"label": "(23000.0,inf)", "max": sys.maxsize}, ],

        "tot_coll_amt": [{"label": "(-inf,3000.0)", "max": 3000.0}, {"label": "(3000.0,15968.0)", "max": 15968.0},
                         {"label": "(15968.0,31935.0)", "max": 31935.0}, {"label": "(31935.0,47903.0)", "max": 47903.0},
                         {"label": "(47903.0,62000.0)", "max": 62000.0},
                         {"label": "(62000.0,inf)", "max": sys.maxsize}, ],

        "tot_cur_bal": [{"label": "(-inf,500000.0)", "max": 500000.0}, {"label": "(500000.0,960199.0)", "max": 960199.0},
                        {"label": "(960199.0,1500000.0)", "max": 1500000.0},
                        {"label": "(1500000.0,inf)", "max": sys.maxsize}, ],

        "total_rev_hi_lim": [{"label": "(-inf,20000.0)", "max": 20000.0}, {"label": "(20000.0,40000.0)", "max": 40000.0},
                             {"label": "(40000.0,60000.0)", "max": 60000.0},
                             {"label": "(60000.0,inf)", "max": sys.maxsize}, ]
        }
