# Customer Churn Prediction

Predict whether a customer will churn using **XGBoost** and **scikit-learn pipelines**.  
The model handles both **categorical** and **numerical features** using `ColumnTransformer` and `OrdinalEncoder`, and is deployable via **Streamlit** for interactive predictions.

---

## 🔹 Live Demo

You can try the interactive web app here:  
[**Customer Churn Prediction App (Streamlit)**]([https://your-streamlit-link.com](https://ecommerce-customer-churn-dataset-apm9nszc5ezdmbirg79qx4.streamlit.app/))  

*(Replace the link with your deployed Streamlit URL)*

---

## ⚙️ Features Used

- Demographics: Age, Gender, Country, City, Signup_Quarter  
- Engagement: Membership_Years, Login_Frequency, Session_Duration_Avg, Pages_Per_Session  
- Purchasing Behavior: Cart_Abandonment_Rate, Wishlist_Items, Total_Purchases, Average_Order_Value, Days_Since_Last_Purchase, Discount_Usage_Rate, Returns_Rate  
- Marketing Interaction: Email_Open_Rate, Customer_Service_Calls, Product_Reviews_Written, Social_Media_Engagement_Score, Mobile_App_Usage, Payment_Method_Diversity, Lifetime_Value, Credit_Balance  

---

## 📊 Model Performance

Trained on 50,000 customers with 20% test split.

| Metric       | Class 0 (Not Churn) | Class 1 (Churn) |
|--------------|-------------------|----------------|
| Precision    | 0.92              | 0.93           |
| Recall       | 0.97              | 0.81           |
| F1-Score     | 0.95              | 0.86           |
| Support      | 7110              | 2890           |

- **Overall Accuracy:** 0.9255 (~93%)  
- Weighted F1-score: 0.92  

> ⚠️ The model performs slightly lower recall on churners (class 1), which may be tuned further using `scale_pos_weight` or threshold adjustments.

---

## 💻 Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd <repo-directory>
