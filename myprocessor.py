class MyProcessor:

    def run(self, df):
        return df.agg(['mean', 'min', 'max'])

    def myFunction(self, data_in):
        self.data_in = data_in
        total_sum = users_count = mean_sum = 0
        users_debts = {}
        users_debts_short = {}
        tmp = {}

        for user in data_in:
            total_sum = total_sum + int(data_in[user])
            users_count = users_count + 1
            mean_sum = total_sum/users_count

        for user in data_in:
            delta_sum_user = mean_sum - int(data_in[user])
            user_delta = {}
            user_delta['sum'] = int(data_in[user])
            if (delta_sum_user >= 0):
                user_delta['debts_out'] = delta_sum_user
                user_delta['debts_in'] = 0
                user_delta['debts_in_total'] = 0
                user_delta['debts'] = {}
            else:
                user_delta['debts_out'] = 0
                user_delta['debts_in'] = abs(delta_sum_user)
                user_delta['debts_in_total'] = abs(delta_sum_user)
                user_delta['debts'] = {}
            users_debts[user] = user_delta

        for user in users_debts:
            users_debts_short[user] = {}
            user_debts_out = users_debts[user].get('debts_out')
            if (user_debts_out > 0):
                for user_other in users_debts:
                    user_other_debts_in = users_debts[user_other].get('debts_in')
                    if (user_debts_out > 0 and user_other_debts_in > 0):
                        if (user_debts_out >= user_other_debts_in):
                            user_debts_out = user_debts_out - user_other_debts_in
                            users_debts[user]['debts'][user_other] = user_other_debts_in
                            users_debts_short[user][user_other] = user_other_debts_in
                            users_debts[user_other]['debts_in'] = 0
                        else:
                            users_debts[user]['debts'][user_other] = user_debts_out
                            users_debts_short[user][user_other] = user_debts_out
                            users_debts[user_other]['debts_in'] = user_other_debts_in - user_debts_out
                            user_debts_out = 0

        data_out = users_debts_short
        data_out_tmp = {"total_sum":total_sum, "users_count":users_count, "mean_sum":mean_sum, "users_debts":users_debts}
        return data_out, data_out_tmp