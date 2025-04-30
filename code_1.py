import streamlit as st
import pandas as pd
import os
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Executive Comparison", page_icon="🧑‍💼", layout="wide")

st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            color: #1e2b3c;
        }
        .stButton button {
            background-color: #4a90e2;
            color: white;
            border-radius: 8px;
        }
        .css-1aumxhk {
            background-color: #ffffff !important;
        }
        .metric-box {
            background-color: #f0f4f8;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        }
        .metric-value {
            font-size: 1.8em;
            font-weight: bold;
            color: #333;
        }
        .metric-label {
            font-size: 0.9em;
            color: #777;
        }
    </style>
""", unsafe_allow_html=True)

json_data = {
    "status": 200,
    "message": "Chart Data Sent Successfully",
    "results": [
        {"assigned_to": 96, "salesPersonName": "Travis Roberson", "totalSalesAmount": 45235.9, "totalSalesCount": 20},
        {"assigned_to": 12, "salesPersonName": "Martez Davis", "totalSalesAmount": 2697437.54, "totalSalesCount": 258},
        {"assigned_to": 8, "salesPersonName": "Charlie Dains", "totalSalesAmount": 3574575.12, "totalSalesCount": 400},
        {"assigned_to": 10, "salesPersonName": "Joel Rivard", "totalSalesAmount": 6009028.35, "totalSalesCount": 397},
        {"assigned_to": 93, "salesPersonName": "Jack Spencer ", "totalSalesAmount": 85868.95, "totalSalesCount": 19},
        {"assigned_to": 97, "salesPersonName": "Carrie  Kirk ", "totalSalesAmount": 34250.02, "totalSalesCount": 10},
        {"assigned_to": 33, "salesPersonName": "James Baxter", "totalSalesAmount": 9643.65, "totalSalesCount": 9},
        {"assigned_to": 13, "salesPersonName": "Marcie Emery", "totalSalesAmount": 0, "totalSalesCount": 2},
        {"assigned_to": 60, "salesPersonName": "Sarah Spillman", "totalSalesAmount": 21684.53, "totalSalesCount": 8},
        {"assigned_to": 35, "salesPersonName": "John Eason", "totalSalesAmount": 12273.31, "totalSalesCount": 2},
        {"assigned_to": 36, "salesPersonName": "Sheena Williams", "totalSalesAmount": 4248.8, "totalSalesCount": 10}
    ]
}

df_executives = pd.DataFrame(json_data['results'])
df_executives.rename(columns={
    "salesPersonName": "Salesperson",
    "totalSalesAmount": "Total Sales ($)",
    "totalSalesCount": "Total Deals Closed"
}, inplace=True)
df_executives = df_executives.sort_values(by="Total Sales ($)", ascending=False)

data_skus = [
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "The Green Halo Ceramic .5g Cartridge - Press Tip Barrel",
            "prod_name": "The Green Halo Ceramic .5g Cartridge - Press Tip Barrel",
            "sku": "TGH_AZ_DOSS_CER_CR_0.5G_BRL",
            "sku_type": None,
            "total_sales": 97200
        }
    },
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "Thunder Canna Custom Rigid Tube for 14pk - Sativa",
            "prod_name": "Thunder Canna Custom Rigid Tubes",
            "sku": "TC_MI_BOX_RT_S",
            "sku_type": "CUSTOM",
            "total_sales": 21900
        }
    },
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "Thunder Canna Custom Rigid Tube for 14pk - Hybrid",
            "prod_name": "Thunder Canna Custom Rigid Tubes",
            "sku": "TC_MI_BOX_RT_H",
            "sku_type": "CUSTOM",
            "total_sales": 43800
        }
    },
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "Thunder Canna Custom Lid for 14pk - Sativa",
            "prod_name": "Thunder Canna Lids",
            "sku": "TC_MI_LID_RT_S",
            "sku_type": "CUSTOM",
            "total_sales": 3600
        }
    },
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "Thunder Canna Custom Rigid Tube for 14pk - Indica",
            "prod_name": "Thunder Canna Custom Rigid Tubes",
            "sku": "TC_MI_BOX_RT_I",
            "sku_type": "CUSTOM",
            "total_sales": 21900
        }
    },
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "Thunder Canna Custom Lid for 14pk - Indica",
            "prod_name": "Thunder Canna Lids",
            "sku": "TC_MI_LID_RT_I",
            "sku_type": "CUSTOM",
            "total_sales": 3600
        }
    },
    {
        "status": 200,
        "message": "Chart Data Sent Successfully",
        "results": {
            "count": 12,
            "item_name": "Thunder Canna Custom Lid for 14pk - Hybrid",
            "prod_name": "Thunder Canna Lids",
            "sku": "TC_MI_LID_RT_H",
            "sku_type": "CUSTOM",
            "total_sales": 7200
        }
    }
]

rows = []
for d in data_skus:
    result = d['results']
    rows.append({
        'Item Name': result['item_name'],
        'Product Name': result['prod_name'],
        'SKU': result['sku'],
        'Total Sales': result['total_sales'],
        'Count': result['count']
    })
df_skus = pd.DataFrame(rows)

sales_data = {
    "status": 200,
    "message": "Chart Data Sent Successfully",
    "results": {
        "monthly_comparison": {
            "April": 1409580.2099999997,
            "March": 1192286.99
        },
        "yearly_comparison": {
            "current_year": {
                "April": 1409580.2099999997,
                "February": 919240.5499999999,
                "January": 945010.0700000002,
                "March": 1192286.99
            },
            "previous_year": {
                "April": 800482.4600000001,
                "August": 864445.1199999999,
                "December": 943133.6700000002,
                "February": 1070272.3599999999,
                "January": 2216030.8099999996,
                "July": 1337715.0199999998,
                "June": 1082858.2599999998,
                "March": 1036901.1200000003,
                "May": 1048604.5299999998,
                "November": 1727541.36,
                "October": 1409813.2800000003,
                "September": 978229.59
            }
        }
    }
}

image_path = os.path.join(os.getcwd(), "image.png")
if os.path.exists(image_path):
    st.sidebar.image(image_path, use_column_width=True)
else:
    st.sidebar.warning("Image not found. Make sure 'image.png' exists in this directory.")

st.sidebar.title("Filters")
selected_salesperson = st.sidebar.selectbox("Select Salesperson", options=["All"] + list(df_executives["Salesperson"].unique()))
if selected_salesperson != "All":
    df_filtered_exec = df_executives[df_executives["Salesperson"] == selected_salesperson]
else:
    df_filtered_exec = df_executives.copy()

total_sales_exec = df_filtered_exec["Total Sales ($)"].sum()
top_person_exec = df_filtered_exec.iloc[0]["Salesperson"]
top_sales_exec = df_filtered_exec.iloc[0]["Total Sales ($)"]
avg_sales_exec = round(total_sales_exec / len(df_filtered_exec), 2) if len(df_filtered_exec) > 0 else 0

st.markdown("## 🧾 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">${total_sales_exec:,.2f}</div>
        <div class="metric-label">Total Sales</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{top_person_exec}</div>
        <div class="metric-label">Top Performer</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">${avg_sales_exec:,.2f}</div>
        <div class="metric-label">Avg Sales per Rep</div>
    </div>
    """, unsafe_allow_html=True)

fig_sales_exec = px.bar(
    df_filtered_exec,
    x="Salesperson",
    y="Total Sales ($)",
    color="Salesperson",
    title="Total Sales by Executive",
    color_discrete_sequence=px.colors.qualitative.Prism
)
fig_sales_exec.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    yaxis_tickprefix="$",
    yaxis_tickformat=",.",
    xaxis_title="Salesperson",
    yaxis_title="Total Sales ($)"
)
st.plotly_chart(fig_sales_exec, use_container_width=True)

fig_deals_exec = px.bar(
    df_filtered_exec,
    x="Salesperson",
    y="Total Deals Closed",
    color="Salesperson",
    title="Total Deals Closed by Executive",
    color_discrete_sequence=px.colors.qualitative.Prism
)
fig_deals_exec.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    xaxis_title="Salesperson",
    yaxis_title="Deals Closed"
)
st.plotly_chart(fig_deals_exec, use_container_width=True)

with st.expander("🔍 View Raw Data"):
    st.dataframe(df_filtered_exec.style.format({"Total Sales ($)": "${:,.2f}"}))

st.sidebar.title("Filters")
selected_product = st.sidebar.selectbox("Select Product", options=["All"] + list(df_skus['Product Name'].unique()))
if selected_product != "All":
    df_filtered_sku = df_skus[df_skus["Product Name"] == selected_product]
else:
    df_filtered_sku = df_skus

total_skus = len(df_filtered_sku)
total_sales_sku = df_filtered_sku['Total Sales'].sum()
avg_sales_sku = round(df_filtered_sku['Total Sales'].mean(), 2)

col1.metric("Total SKUs", total_skus)
col2.metric("Total Sales", f"${total_sales_sku:,.2f}")
col3.metric("Average Sales per SKU", f"${avg_sales_sku:,.2f}")

fig_sku = px.bar(
    df_filtered_sku,
    x='SKU',
    y='Total Sales',
    color='Product Name',
    hover_data=['Item Name', 'Count'],
    title="Total Sales by SKU",
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig_sku.update_layout(
    xaxis_title="SKU",
    yaxis_title="Total Sales ($)",
    plot_bgcolor='white',
    paper_bgcolor='rgba(0,0,0,0)',
    legend_title_text='Product'
)
st.plotly_chart(fig_sku, use_container_width=True)

with st.expander("🔍 View Raw Data (SKUs)"):
    st.dataframe(df_filtered_sku.style.format({'Total Sales': "${:,.2f}"}))

st.title("Sales Comparison Dashboard")
st.subheader("Monthly Comparison: Current vs Previous Month")
monthly_data = sales_data['results']['monthly_comparison']
values = list(monthly_data.values())
fig1, ax1 = plt.subplots()
bars = ax1.bar(['Previous Month', 'Current Month'], values, color=['#4E79A7', '#F28E2B'])
ax1.set_ylabel('Sales Amount')
ax1.set_title('Month-over-Month Sales Comparison')
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 20000, f'{yval:,.2f}', ha='center', fontsize=10)
st.pyplot(fig1)

st.subheader("Yearly Comparison: Current Year vs Previous Year")
current_year = sales_data['results']['yearly_comparison']['current_year']
previous_year = sales_data['results']['yearly_comparison']['previous_year']
all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
current_values = [current_year.get(month, 0) for month in all_months]
previous_values = [previous_year.get(month, 0) for month in all_months]
x_indexes = range(len(all_months))
fig2, ax2 = plt.subplots(figsize=(12, 6))
bar_width = 0.35
rects1 = ax2.bar([i - bar_width/2 for i in x_indexes], current_values, width=bar_width, label='Current Year', color='#4E79A7')
rects2 = ax2.bar([i + bar_width/2 for i in x_indexes], previous_values, width=bar_width, label='Previous Year', color='#F28E2B')
ax2.set_xlabel('Months')
ax2.set_ylabel('Sales Amount')
ax2.set_title('Monthly Sales Comparison: Current vs Previous Year')
ax2.set_xticks(x_indexes)
ax2.set_xticklabels(all_months, rotation=45)
ax2.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height > 0:
            ax2.annotate(f'{height:,.2f}',
                         xy=(rect.get_x() + rect.get_width() / 2, height),
                         xytext=(0, 3),
                         textcoords="offset points",
                         ha='center', va='bottom', fontsize=8)

autolabel(rects1)
autolabel(rects2)
fig2.tight_layout()
st.pyplot(fig2)