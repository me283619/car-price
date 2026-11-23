{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "initial_id",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2026-11-23T06:27:01.003534200Z",
     "start_time": "2026-11-23T06:26:53.951546500Z"
    },
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\AppData\\Local\\Temp\\ipykernel_7704\\3549283406.py:61: UserWarning: The parameters have been moved from the Blocks constructor to the launch() method in Gradio 6.0: theme, css. Please pass these parameters to launch() instead.\n",
      "  with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7860\n",
      "* To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7860/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "# 1. تحميل الموديل والأدوات المحفوظة\n",
    "bundle = joblib.load(\"car_price_model.pkl\")\n",
    "model = bundle[\"model\"]\n",
    "encoders = bundle[\"encoders\"]\n",
    "scaler = bundle[\"scaler\"]\n",
    "features = bundle[\"features\"]\n",
    "\n",
    "# 2. قوائم الاختيارات للـ Dropdowns\n",
    "if \"df\" in globals():\n",
    "    models_list = sorted(df[\"model\"].astype(str).str.strip().unique().tolist())\n",
    "    trans_list = sorted(\n",
    "        df[\"transmission\"].astype(str).str.strip().unique().tolist()\n",
    "    )\n",
    "    fuel_list = sorted(df[\"fueltype\"].astype(str).str.strip().unique().tolist())\n",
    "else:\n",
    "    models_list = [\"Golf\", \"Polo\", \"Passat\", \"Tiguan\", \"Fiesta\", \"Focus\", \"Beetle\"]\n",
    "    trans_list = [\"Manual\", \"Automatic\", \"Semi-Auto\"]\n",
    "    fuel_list = [\"Petrol\", \"Diesel\", \"Hybrid\", \"Electric\"]\n",
    "\n",
    "\n",
    "# 3. دالة التنبؤ\n",
    "def predict_car_price(\n",
    "        model_name, year, mileage, tax, mpg, enginesize, transmission, fueltype\n",
    "):\n",
    "    input_df = pd.DataFrame([{\n",
    "        \"model\": str(model_name).strip(),\n",
    "        \"year\": int(year),\n",
    "        \"mileage\": float(mileage),\n",
    "        \"tax\": float(tax),\n",
    "        \"mpg\": float(mpg),\n",
    "        \"enginesize\": float(enginesize),\n",
    "        \"transmission\": str(transmission).strip(),\n",
    "        \"fueltype\": str(fueltype).strip(),\n",
    "    }])\n",
    "\n",
    "    for col, enc in encoders.items():\n",
    "        if col in input_df.columns:\n",
    "            input_df[col] = enc.transform(input_df[[col]])\n",
    "\n",
    "    input_df = input_df[features]\n",
    "    input_scaled = scaler.transform(input_df)\n",
    "    pred_price = model.predict(input_scaled)[0]\n",
    "\n",
    "    return (\n",
    "        f\"### £ {pred_price:,.2f}\\n\"\n",
    "        f\"**الموديل:** {model_name} | **السنة:** {int(year)} | **الممشى:**\"\n",
    "        f\" {int(mileage):,} mi\"\n",
    "    )\n",
    "\n",
    "\n",
    "# 4. تصميم الواجهة بـ gr.Blocks\n",
    "custom_css = \"\"\"\n",
    ".gradio-container { max-width: 980px !important; margin: auto !important; }\n",
    ".result-box { border: 1px solid #3b82f6; border-radius: 12px; padding: 16px; }\n",
    "\"\"\"\n",
    "\n",
    "with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:\n",
    "    gr.Markdown(\n",
    "        \"# 🚗 نظام توقع أسعار السيارات\\nتقدير فوري للسعر باستخدام نموذج **Random Forest** (بيانات سوق السيارات البريطاني).\")\n",
    "\n",
    "    with gr.Row():\n",
    "        with gr.Column(scale=1):\n",
    "            gr.Markdown(\"### 📋 البيانات الأساسية\")\n",
    "            model_input = gr.Dropdown(\n",
    "                choices=models_list,\n",
    "                value=models_list[0] if models_list else None,\n",
    "                label=\"الموديل (Model)\",\n",
    "            )\n",
    "            year_input = gr.Number(label=\"سنة الصنع (Year)\", value=2019, precision=0)\n",
    "            mileage_input = gr.Number(label=\"الممشى (Mileage)\", value=22000)\n",
    "            trans_input = gr.Dropdown(\n",
    "                choices=trans_list,\n",
    "                value=trans_list[0] if trans_list else None,\n",
    "                label=\"ناقل الحركة (Transmission)\",\n",
    "            )\n",
    "\n",
    "        with gr.Column(scale=1):\n",
    "            gr.Markdown(\"### ⚙️ المواصفات الفنية\")\n",
    "            fuel_input = gr.Dropdown(\n",
    "                choices=fuel_list,\n",
    "                value=fuel_list[0] if fuel_list else None,\n",
    "                label=\"نوع الوقود (Fuel Type)\",\n",
    "            )\n",
    "            engine_input = gr.Number(\n",
    "                label=\"سعة المحرك باللتر (Engine Size)\", value=1.6\n",
    "            )\n",
    "            mpg_input = gr.Number(label=\"استهلاك الوقود (MPG)\", value=52.0)\n",
    "            tax_input = gr.Number(label=\"الضريبة السنوية (Tax)\", value=145)\n",
    "\n",
    "    predict_btn = gr.Button(\"🔍 احسب السعر المتوقع\", variant=\"primary\", size=\"lg\")\n",
    "\n",
    "    with gr.Group(elem_classes=\"result-box\"):\n",
    "        gr.Markdown(\"### 💰 السعر التقديري\")\n",
    "        output_box = gr.Markdown(\n",
    "            \"أدخل بيانات السيارة واضغط على **احسب السعر المتوقع** لعرض النتيجة.\"\n",
    "        )\n",
    "\n",
    "    gr.Examples(\n",
    "        examples=[\n",
    "            [\"Golf\", 2019, 18000, 145, 55.0, 1.5, \"Manual\", \"Petrol\"],\n",
    "            [\"Polo\", 2017, 35000, 20, 60.0, 1.0, \"Manual\", \"Petrol\"],\n",
    "            [\"Tiguan\", 2020, 15000, 150, 44.0, 2.0, \"Automatic\", \"Diesel\"],\n",
    "        ],\n",
    "        inputs=[\n",
    "            model_input,\n",
    "            year_input,\n",
    "            mileage_input,\n",
    "            tax_input,\n",
    "            mpg_input,\n",
    "            engine_input,\n",
    "            trans_input,\n",
    "            fuel_input,\n",
    "        ],\n",
    "        outputs=output_box,\n",
    "        fn=predict_car_price,\n",
    "        cache_examples=False,\n",
    "        label=\"أمثلة سريعة للتجربة\",\n",
    "    )\n",
    "\n",
    "    predict_btn.click(\n",
    "        fn=predict_car_price,\n",
    "        inputs=[\n",
    "            model_input,\n",
    "            year_input,\n",
    "            mileage_input,\n",
    "            tax_input,\n",
    "            mpg_input,\n",
    "            engine_input,\n",
    "            trans_input,\n",
    "            fuel_input,\n",
    "        ],\n",
    "        outputs=output_box,\n",
    "    )\n",
    "\n",
    "import os\n",
    "port=int(os.environ.get(\"PORT\", 7860))\n",
    "demo.launch(server_name=\"0.0.0.0\",server_port=port)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
