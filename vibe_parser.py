from copy import copy
from base_parser import BaseParser

class VibeParser(BaseParser):
    charges_container = []
    subscription_container = []
    account_container = []
    statement_container = []
    adjusting_list = []
    foot_note_container = []

    def set_containers(self):
        self.set_account_summary()
        self.set_statement_summary()
        self.set_charges_container()
        self.set_subscriptions_container()
        self.set_footnote_container()

    def set_charges_container(self):
        index = self.get_index_of_value("Charges For This Month", 1)
        buffer = self.config.buffers['CHARGES_HEADERS']
        count = 0
        for i in range(index, index + buffer + 1):
            key = self.current_list[i]
            value = self.current_list[i + buffer]
            self.charges_container.append([key, value])
            count += 1

        totalKey = self.current_list[index + buffer + count]
        totalValue = self.current_list[index + buffer + count + 1]
        self.charges_container.append([totalKey, totalValue])

    def set_subscriptions_container(self):
        index = self.get_index_of_value("Subscription Charges")
        buffer = self.config.buffers['SUBSCRIPTION_HEADERS']
        for i in range(index, index + buffer + 1):
            key = self.current_list[i]
            value = self.current_list[i + buffer]
            self.subscription_container.append([key, value])

    def set_account_summary(self):
        self.adjusting_list = copy(self.current_list)
        index = self.get_index_of_value("Account Number")
        buffer = self.config.buffers['ACCOUNT_ITEMS']

        for i in range(index, index + buffer):
            top_location = self.current_list[i][1][1].strip()
            key = self.current_list[i]
            j = i + buffer
            value = self.current_list[j]
            self.account_container.append([key, value])

    def set_statement_summary(self):
        index = self.get_index_of_value("Statement Summary:") + 1
        buffer = self.config.buffers['STATEMENT_ITEMS']
        for i in range(index, index + buffer):
            top_location = self.current_list[i][1][1].strip()
            key = self.current_list[i]
            j = i + buffer
            value = self.current_list[j]
            self.statement_container.append([key, value])

    def set_footnote_container(self):
        index = self.get_index_of_substring("PAY IN FULL : ") - 1
        buffer = self.config.buffers['FOOTNOTE_ITEMS']

        for i in range(buffer):
            insert_index = buffer - i - 1
            value = self.current_list[index - i]
            self.foot_note_container.insert(insert_index, value)

    def get_company_name_value(self):
        return self.current_list[0][0]

    def get_tmp_list(self):
        for elem in self.adjusting_list:
            print (elem)

    def get_company_address_value(self):
        index = self.get_index_of_value("Statement Summary:")
        address = ""
        for i in range(1, index):
            address += self.current_list[i][0]
        return address

    def get_pay_in_full_value(self):
        for item in self.current_list:
            if "PAY IN FULL : " in item[0]:
                return item[0].replace("PAY IN FULL : ", "")

    def get_charges_value(self, key):
        return self.get_from_container(key, self.charges_container)

    def get_subscriptions_value(self, key):
        return self.get_from_container(key, self.subscription_container)

    def get_account_summary_value(self, key):
        return self.get_from_container(key, self.account_container)

    def get_statement_summary_value(self, key):
        return self.get_from_container(key, self.statement_container)

    def print_charges_value(self, key):
        value = self.get_charges_value(key)
        print (key + " : " + value)

    def print_subscriptions_value(self, key):
        value = self.get_subscriptions_value(key)
        print (key + " : " + value)

    def print_account_summary_value(self, key):
        value = self.get_account_summary_value(key)
        print (key + " : " + value)

    def print_statement_summary_value(self, key):
        value = self.get_statement_summary_value(key)
        print (key + " : " + value)

    def get_footnote_value(self, item):
        return self.foot_note_container[item][0]
