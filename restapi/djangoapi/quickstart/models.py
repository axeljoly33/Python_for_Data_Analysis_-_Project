from django.db import models

# Create your models here.


class Companies(models.Model):
    year = models.TextField(blank=True, null=True)
    row = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, primary_key=True)
    # Field renamed to remove unsuitable characters.
    net_profit_total_assets = models.FloatField(
        db_column='net profit / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    total_liabilities_total_assets = models.FloatField(
        db_column='total liabilities / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    working_capital_total_assets = models.FloatField(
        db_column='working capital / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    current_assets_short_term_liabilities = models.FloatField(
        db_column='current assets / short-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_cash_short_term_securities_receivables_short_term_liabilities_operating_expenses_depreciation_365 = models.FloatField(
        db_column='[(cash + short-term securities + receivables - short-term liabilities) / (operating expenses - depreciation)] * 365', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    retained_earnings_total_assets = models.FloatField(
        db_column='retained earnings / total assets', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebit_total_assets = models.FloatField(
        db_column='EBIT / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    book_value_of_equity_total_liabilities = models.FloatField(
        db_column='book value of equity / total liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    sales_total_assets = models.FloatField(
        db_column='sales / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    equity_total_assets = models.FloatField(
        db_column='equity / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gross_profit_extraordinary_items_financial_expenses_total_assets = models.FloatField(
        db_column='(gross profit + extraordinary items + financial expenses) / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    gross_profit_short_term_liabilities = models.FloatField(
        db_column='gross profit / short-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gross_profit_depreciation_sales = models.FloatField(
        db_column='(gross profit + depreciation) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gross_profit_interest_total_assets = models.FloatField(
        db_column='(gross profit + interest) / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_total_liabilities_365_gross_profit_depreciation_field = models.FloatField(
        db_column='(total liabilities * 365) / (gross profit + depreciation)', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gross_profit_depreciation_total_liabilities = models.FloatField(
        db_column='(gross profit + depreciation) / total liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    total_assets_total_liabilities = models.FloatField(
        db_column='total assets / total liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    gross_profit_total_assets = models.FloatField(
        db_column='gross profit / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    gross_profit_sales = models.FloatField(
        db_column='gross profit / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_inventory_365_sales = models.FloatField(
        db_column='(inventory * 365) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sales_n_sales_n_1_field = models.FloatField(
        db_column='sales (n) / sales (n-1)', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    profit_on_operating_activities_total_assets = models.FloatField(
        db_column='profit on operating activities / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    net_profit_sales = models.FloatField(
        db_column='net profit / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    gross_profit_in_3_years_total_assets = models.FloatField(
        db_column='gross profit (in 3 years) / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_equity_share_capital_total_assets = models.FloatField(
        db_column='(equity - share capital) / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_net_profit_depreciation_total_liabilities = models.FloatField(
        db_column='(net profit + depreciation) / total liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    profit_on_operating_activities_financial_expenses = models.FloatField(
        db_column='profit on operating activities / financial expenses', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    working_capital_fixed_assets = models.FloatField(
        db_column='working capital / fixed assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    logarithm_of_total_assets = models.FloatField(
        db_column='logarithm of total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_total_liabilities_cash_sales = models.FloatField(
        db_column='(total liabilities - cash) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_gross_profit_interest_sales = models.FloatField(
        db_column='(gross profit + interest) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_liabilities_365_cost_of_products_sold = models.FloatField(
        db_column='(current liabilities * 365) / cost of products sold', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    operating_expenses_short_term_liabilities = models.FloatField(
        db_column='operating expenses / short-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    operating_expenses_total_liabilities = models.FloatField(
        db_column='operating expenses / total liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    profit_on_sales_total_assets = models.FloatField(
        db_column='profit on sales / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    total_sales_total_assets = models.FloatField(
        db_column='total sales / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_assets_inventories_long_term_liabilities = models.FloatField(
        db_column='(current assets - inventories) / long-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    constant_capital_total_assets = models.FloatField(
        db_column='constant capital / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    profit_on_sales_sales = models.FloatField(
        db_column='profit on sales / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_assets_inventory_receivables_short_term_liabilities = models.FloatField(
        db_column='(current assets - inventory - receivables) / short-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_liabilities_profit_on_operating_activities_depreciation_12_365_field = models.FloatField(
        db_column='total liabilities / ((profit on operating activities + depreciation) * (12/365))', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    profit_on_operating_activities_sales = models.FloatField(
        db_column='profit on operating activities / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    rotation_receivables_inventory_turnover_in_days = models.FloatField(
        db_column='rotation receivables + inventory turnover in days', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_receivables_365_sales = models.FloatField(
        db_column='(receivables * 365) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    net_profit_inventory = models.FloatField(
        db_column='net profit / inventory', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_current_assets_inventory_short_term_liabilities = models.FloatField(
        db_column='(current assets - inventory) / short-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_inventory_365_cost_of_products_sold = models.FloatField(
        db_column='(inventory * 365) / cost of products sold', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebitda_profit_on_operating_activities_depreciation_total_assets = models.FloatField(
        db_column='EBITDA (profit on operating activities - depreciation) / total assets', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    ebitda_profit_on_operating_activities_depreciation_sales = models.FloatField(
        db_column='EBITDA (profit on operating activities - depreciation) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    current_assets_total_liabilities = models.FloatField(
        db_column='current assets / total liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    short_term_liabilities_total_assets = models.FloatField(
        db_column='short-term liabilities / total assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_short_term_liabilities_365_cost_of_products_sold_field = models.FloatField(
        db_column='(short-term liabilities * 365) / cost of products sold)', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    equity_fixed_assets = models.FloatField(
        db_column='equity / fixed assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    constant_capital_fixed_assets = models.FloatField(
        db_column='constant capital / fixed assets', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    working_capital = models.FloatField(
        db_column='working capital', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_sales_cost_of_products_sold_sales = models.FloatField(
        db_column='(sales - cost of products sold) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_current_assets_inventory_short_term_liabilities_sales_gross_profit_depreciation_field = models.FloatField(
        db_column='(current assets - inventory - short-term liabilities) / (sales - gross profit - depreciation)', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    total_costs_total_sales = models.FloatField(
        db_column='total costs /total sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    long_term_liabilities_equity = models.FloatField(
        db_column='long-term liabilities / equity', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    sales_inventory = models.FloatField(
        db_column='sales / inventory', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    sales_receivables = models.FloatField(
        db_column='sales / receivables', blank=True, null=True)
    # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_short_term_liabilities_365_sales = models.FloatField(
        db_column='(short-term liabilities *365) / sales', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    sales_short_term_liabilities = models.FloatField(
        db_column='sales / short-term liabilities', blank=True, null=True)
    # Field renamed to remove unsuitable characters.
    sales_fixed_assets = models.FloatField(
        db_column='sales / fixed assets', blank=True, null=True)
    # Field name made lowercase. Field renamed because it was a Python reserved word.
    class_field = models.IntegerField(db_column='Class', blank=True, null=True)

    class Meta:
        db_table = 'Companies'
