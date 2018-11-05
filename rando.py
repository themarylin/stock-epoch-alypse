from random import random, randint
def randomStock(rand_stock,results):
    stk_rand_stock_list =[]
    stk_rand_date_list =[]
    stk_rand_adj_close_list =[]
    stk_rand_comp_earning_list =[]

    prev_stock = 0
    curr_comp_earn = 1
    prev_adj_close = 0

    for stk_rand in results:
        stk_rand_stock_list.append(stk_rand.stock)
        stk_rand_date_list.append(stk_rand.date)
        stk_rand_adj_close_list.append(stk_rand.adj_close)
        curr_stock = random() < 0.5
        if curr_stock == False:
            curr_stock= 0
        else:
            curr_stock= 1
        sellbuy_scen = random() < 0.5
        if sellbuy_scen == False:
            sellbuy_scen= 0
        else:
            sellbuy_scen= 1

        if prev_adj_close == 0:
            prev_adj_close = stk_rand.adj_close
        curr_adj_close = stk_rand.adj_close
        if prev_stock == 0 and curr_stock == 0:
            stk_rand_comp_earning_list.append(curr_comp_earn)
            prev_adj_close=curr_adj_close
            continue
        if prev_stock == 0 and curr_stock == 1:
            prev_stock = 1
            stk_rand_comp_earning_list.append(curr_comp_earn)
            prev_adj_close=curr_adj_close
            continue
        if prev_stock == 1 and curr_stock == 1:
            stk_rand_comp_earning_list.append(curr_comp_earn)
            prev_adj_close=curr_adj_close
            continue
        if prev_stock == 1 and curr_stock == 0:
            if sellbuy_scen == 0:
                curr_comp_earn=(((curr_adj_close-prev_adj_close)/prev_adj_close)+1)*curr_comp_earn
                prev_stock = 0
            else:
                curr_comp_earn=(((curr_adj_close-prev_adj_close)/prev_adj_close)+1)*curr_comp_earn
        stk_rand_comp_earning_list.append(curr_comp_earn)
        prev_adj_close=curr_adj_close
    stk_rand_adj_comp_earning_list = [value-1 for value in stk_rand_comp_earning_list]

    data = [{
        "date":stk_rand_date_list[i].strftime("%Y-%m-%d"),
        "adj_close":stk_rand_adj_close_list[i],
        "adj_comp_earning":stk_rand_adj_comp_earning_list[i]
    } for i in range(len(stk_rand_date_list))]

    return [
        {
            "stock":rand_stock,
            "data":data
        }
    ]
