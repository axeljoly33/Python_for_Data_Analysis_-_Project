from djangoapi.quickstart.models import Companies
from rest_framework import serializers


class CompaniesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Companies
        fields = [
            "year",
            "row",
            "id",
            "net_profit_total_assets",
            "total_liabilities_total_assets",
            "working_capital_total_assets",
            "current_assets_short_term_liabilities",
            "field_cash_short_term_securities_receivables_short_term_liabilities_operating_expenses_depreciation_365",
            "retained_earnings_total_assets",
            "ebit_total_assets",
            "book_value_of_equity_total_liabilities",
            "sales_total_assets",
            "equity_total_assets",
            "field_gross_profit_extraordinary_items_financial_expenses_total_assets",
            "gross_profit_short_term_liabilities",
            "field_gross_profit_depreciation_sales",
            "field_gross_profit_interest_total_assets",
            "field_total_liabilities_365_gross_profit_depreciation_field",
            "field_gross_profit_depreciation_total_liabilities",
            "total_assets_total_liabilities",
            "gross_profit_total_assets",
            "gross_profit_sales",
            "field_inventory_365_sales",
            "sales_n_sales_n_1_field",
            "profit_on_operating_activities_total_assets",
            "net_profit_sales",
            "gross_profit_in_3_years_total_assets",
            "field_equity_share_capital_total_assets",
            "field_net_profit_depreciation_total_liabilities",
            "profit_on_operating_activities_financial_expenses",
            "working_capital_fixed_assets",
            "logarithm_of_total_assets",
            "field_total_liabilities_cash_sales",
            "field_gross_profit_interest_sales",
            "field_current_liabilities_365_cost_of_products_sold",
            "operating_expenses_short_term_liabilities",
            "operating_expenses_total_liabilities",
            "profit_on_sales_total_assets",
            "total_sales_total_assets",
            "field_current_assets_inventories_long_term_liabilities",
            "constant_capital_total_assets",
            "profit_on_sales_sales",
            "field_current_assets_inventory_receivables_short_term_liabilities",
            "total_liabilities_profit_on_operating_activities_depreciation_12_365_field",
            "profit_on_operating_activities_sales",
            "rotation_receivables_inventory_turnover_in_days",
            "field_receivables_365_sales",
            "net_profit_inventory",
            "field_current_assets_inventory_short_term_liabilities",
            "field_inventory_365_cost_of_products_sold",
            "ebitda_profit_on_operating_activities_depreciation_total_assets",
            "ebitda_profit_on_operating_activities_depreciation_sales",
            "current_assets_total_liabilities",
            "short_term_liabilities_total_assets",
            "field_short_term_liabilities_365_cost_of_products_sold_field",
            "equity_fixed_assets",
            "constant_capital_fixed_assets",
            "working_capital",
            "field_sales_cost_of_products_sold_sales",
            "field_current_assets_inventory_short_term_liabilities_sales_gross_profit_depreciation_field",
            "total_costs_total_sales",
            "long_term_liabilities_equity",
            "sales_inventory",
            "sales_receivables",
            "field_short_term_liabilities_365_sales",
            "sales_short_term_liabilities",
            "sales_fixed_assets",
            "class_field"
        ]
