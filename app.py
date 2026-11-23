
import gradio as gr
import json
import joblib
import pandas as pd

# 1. تحميل الموديل والأدوات المحفوظة
bundle = joblib.load("car_price_model.pkl")
model = bundle["model"]
encoders = bundle["encoders"]
scaler = bundle["scaler"]
features = bundle["features"]

# 2. قوائم الاختيارات للـ Dropdowns
with open("options.json", encoding="utf-8") as f:
    opts = json.load(f)
models_list = opts["models"]
trans_list = opts["transmissions"]
fuel_list = opts["fuel_types"]


# 3. دالة التنبؤ
def predict_car_price(
        model_name, year, mileage, tax, mpg, enginesize, transmission, fueltype
):
    input_df = pd.DataFrame([{
        "model": str(model_name).strip(),
        "year": int(year),
        "mileage": float(mileage),
        "tax": float(tax),
        "mpg": float(mpg),
        "enginesize": float(enginesize),
        "transmission": str(transmission).strip(),
        "fueltype": str(fueltype).strip(),
    }])

    for col, enc in encoders.items():
        if col in input_df.columns:
            input_df[col] = enc.transform(input_df[[col]])

    input_df = input_df[features]
    input_scaled = scaler.transform(input_df)
    pred_price = model.predict(input_scaled)[0]

    return (
        f"### £ {pred_price:,.2f}\n"
        f"**الموديل:** {model_name} | **السنة:** {int(year)} | **الممشى:**"
        f" {int(mileage):,} mi"
    )


# 4. تصميم الواجهة بـ gr.Blocks
custom_css = """
.gradio-container { max-width: 980px !important; margin: auto !important; }
.result-box { border: 1px solid #3b82f6; border-radius: 12px; padding: 16px; }
"""

with gr.Blocks() as demo:
    gr.Markdown(
        "# 🚗 نظام توقع أسعار السيارات\nتقدير فوري للسعر باستخدام نموذج **Random Forest** (بيانات سوق السيارات البريطاني).")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📋 البيانات الأساسية")
            model_input = gr.Dropdown(
                choices=models_list,
                value=models_list[0] if models_list else None,
                label="الموديل (Model)",
            )
            year_input = gr.Number(label="سنة الصنع (Year)", value=2019, precision=0)
            mileage_input = gr.Number(label="الممشى (Mileage)", value=22000)
            trans_input = gr.Dropdown(
                choices=trans_list,
                value=trans_list[0] if trans_list else None,
                label="ناقل الحركة (Transmission)",
            )

        with gr.Column(scale=1):
            gr.Markdown("### ⚙️ المواصفات الفنية")
            fuel_input = gr.Dropdown(
                choices=fuel_list,
                value=fuel_list[0] if fuel_list else None,
                label="نوع الوقود (Fuel Type)",
            )
            engine_input = gr.Number(
                label="سعة المحرك باللتر (Engine Size)", value=1.6
            )
            mpg_input = gr.Number(label="استهلاك الوقود (MPG)", value=52.0)
            tax_input = gr.Number(label="الضريبة السنوية (Tax)", value=145)

    predict_btn = gr.Button("🔍 احسب السعر المتوقع", variant="primary", size="lg")

    with gr.Group(elem_classes="result-box"):
        gr.Markdown("### 💰 السعر التقديري")
        output_box = gr.Markdown(
            "أدخل بيانات السيارة واضغط على **احسب السعر المتوقع** لعرض النتيجة."
        )

    gr.Examples(
        examples=[
            ["Golf", 2019, 18000, 145, 55.0, 1.5, "Manual", "Petrol"],
            ["Polo", 2017, 35000, 20, 60.0, 1.0, "Manual", "Petrol"],
            ["Tiguan", 2020, 15000, 150, 44.0, 2.0, "Automatic", "Diesel"],
        ],
        inputs=[
            model_input,
            year_input,
            mileage_input,
            tax_input,
            mpg_input,
            engine_input,
            trans_input,
            fuel_input,
        ],
        outputs=output_box,
        fn=predict_car_price,
        cache_examples=False,
        label="أمثلة سريعة للتجربة",
    )

    predict_btn.click(
        fn=predict_car_price,
        inputs=[
            model_input,
            year_input,
            mileage_input,
            tax_input,
            mpg_input,
            engine_input,
            trans_input,
            fuel_input,
        ],
        outputs=output_box,
    )

import os
port=int(os.environ.get("PORT", 7860))
demo.launch(server_name="0.0.0.0",server_port=port,theme=gr.themes.Soft(),css=custom_css)
