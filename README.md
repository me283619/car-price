# 🚗 Car Price Prediction — End-to-End Machine Learning Project

مشروع Machine Learning متكامل للتنبؤ بأسعار السيارات المستعملة، من تجميع البيانات وحتى بناء تطبيق تفاعلي جاهز للتجربة.

## 📊 النتائج

| Model | R² Score |
|---|---|
| Linear Regression (Baseline) | 0.87 |
| Random Forest (بعد GridSearch) | **0.95** |

تمت مقارنة أداء التدريب والاختبار (Train vs. Test) للتأكد من عدم وجود Overfitting، وجاء الأداء متوازناً ومستقراً.

## 🔄 خطوات المشروع

### 1. Data Collection & Consolidation
كانت البيانات موزعة على عدة ملفات، كل ملف خاص بأنواع معينة من السيارات. تم تجميعها في dataset موحدة، وتوحيد الأعمدة لضمان اتساقها وجاهزيتها للتحليل.

### 2. Data Cleaning & Outlier Handling
- تنظيف البيانات ومعالجة القيم.
- اكتشاف القيم المتطرفة (Outliers) باستخدام **Isolation Forest**.
- معالجتها بأسلوب **Clipping** للحد من تأثيرها على النموذج.

### 3. Exploratory Data Analysis (EDA)
- عدة Visualizations لفهم توزيع البيانات، وأظهرت النتائج أن السيارات ذات ناقل الحركة المانيوال هي الأكثر استخداماً.
- **Correlation Heatmap** لمعرفة أكثر العوامل ارتباطاً بالسعر، وكانت سنة الصنع (Year) من أقوى العوامل المؤثرة.

### 4. Preprocessing & Modeling
- تقسيم البيانات إلى Train / Test.
- **TargetEncoder** للأعمدة الفئوية و**StandardScaler** للأعمدة الرقمية.
- البدء بـ Linear Model كـ Baseline، ثم الانتقال إلى **Random Forest**.
- ضبط الـ Hyperparameters باستخدام **GridSearchCV**.

### 5. Saving & Interactive Demo
- حفظ النموذج مع مكونات المعالجة (Encoder و Scaler).
- بناء واجهة تفاعلية باستخدام **Gradio** لتجربة التنبؤ بأسعار السيارات بشكل مباشر.

## 🛠️ التقنيات المستخدمة

`Python` · `Pandas` · `NumPy` · `Matplotlib / Seaborn` · `Scikit-learn` · `Gradio`

## ▶️ طريقة التشغيل

```bash
# 1. استنساخ المشروع
git clone <repo-url>
cd <project-folder>

# 2. تشغيل التطبيق
python app.py
```

> عدّل اسم الرابط واسم ملف التشغيل حسب هيكل المشروع عندك.

## 👤 المطور

**Mahmoud Essam Mahmoud**
Faculty of Computers and Artificial Intelligence — Benha University
