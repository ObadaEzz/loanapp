# نظام الموافقة على القروض - Loan Approval System

## نظرة عامة
نظام ذكي لتقييم طلبات القروض باستخدام تقنيات التعلم الآلي. يتيح النظام للمستخدمين إدخال بياناتهم والحصول على تقييم فوري لاحتمالية الموافقة على القرض.

## المميزات
- واجهة ويب سهلة الاستخدام
- نموذج تعلم آلي متقدم للتنبؤ
- تحليل البيانات الاستكشافي (EDA)
- قاعدة بيانات لتخزين الطلبات
- رسوم بيانية تفاعلية

## التقنيات المستخدمة
- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn, XGBoost
- **Database**: SQLite
- **Visualization**: Plotly, Matplotlib
- **Deployment**: Vercel

## التثبيت المحلي

### المتطلبات
- Python 3.9+
- pip

### خطوات التثبيت
1. استنسخ المشروع:
```bash
git clone <repository-url>
cd MLT_project-loan-approval-system-
```

2. أنشئ بيئة افتراضية:
```bash
python -m venv venv
source venv/bin/activate  # على Linux/Mac
# أو
venv\Scripts\activate  # على Windows
```

3. ثبت المتطلبات:
```bash
pip install -r requirements.txt
```

4. شغل التطبيق:
```bash
python flask_app.py
```

5. افتح المتصفح على: `http://localhost:5000`

## النشر على Vercel

### المتطلبات
- حساب على [Vercel](https://vercel.com)
- Vercel CLI (اختياري)

### خطوات النشر

#### الطريقة الأولى: عبر GitHub
1. ارفع الكود إلى GitHub
2. اربط حساب Vercel بحساب GitHub
3. اختر المشروع من Vercel Dashboard
4. اضغط "Deploy"

#### الطريقة الثانية: عبر Vercel CLI
1. ثبت Vercel CLI:
```bash
npm i -g vercel
```

2. سجل دخولك:
```bash
vercel login
```

3. انشر المشروع:
```bash
vercel
```

### ملاحظات مهمة للنشر على Vercel
- قاعدة البيانات ستكون في الذاكرة (in-memory) على Vercel
- البيانات ستختفي عند إعادة تشغيل الخدمة
- للنشر الإنتاجي، استخدم قاعدة بيانات خارجية مثل PostgreSQL

## هيكل المشروع
```
MLT_project-loan-approval-system-/
├── api/
│   ├── index.py          # التطبيق الرئيسي لـ Vercel
│   └── wsgi.py           # نقطة دخول WSGI
├── templates/            # قوالب HTML
├── static/              # الملفات الثابتة
├── models_analytics/    # النماذج والتحليلات
├── flask_app.py         # التطبيق المحلي
├── requirements.txt     # متطلبات Python
├── vercel.json          # إعدادات Vercel
├── runtime.txt          # إصدار Python
└── .vercelignore        # ملفات متجاهلة في Vercel
```

## الاستخدام
1. **الصفحة الرئيسية**: نظرة عامة على النظام
2. **إضافة طلب**: إدخال بيانات طلب قرض جديد
3. **عرض الطلبات**: مراجعة جميع الطلبات المقدمة
4. **تحليل البيانات**: رسوم بيانية وتحليلات
5. **مقاييس النموذج**: أداء النموذج الإحصائي

## المساهمة
نرحب بالمساهمات! يرجى:
1. عمل Fork للمشروع
2. إنشاء branch جديد للميزة
3. عمل Commit للتغييرات
4. عمل Push للـ branch
5. إنشاء Pull Request

## الترخيص
هذا المشروع مرخص تحت رخصة MIT.

## الدعم
لأي استفسارات أو مشاكل، يرجى فتح issue في GitHub.

