# دليل النشر على Vercel - Deployment Guide

## نظرة عامة
هذا الدليل يوضح كيفية نشر تطبيق نظام الموافقة على القروض على منصة Vercel.

## المتطلبات المسبقة
1. حساب على [Vercel](https://vercel.com)
2. حساب على [GitHub](https://github.com) (مفضل)
3. Vercel CLI (اختياري)

## خطوات النشر

### الطريقة الأولى: النشر عبر GitHub (موصى بها)

#### 1. رفع الكود إلى GitHub
```bash
# تهيئة Git repository
git init
git add .
git commit -m "Initial commit for Vercel deployment"

# رفع إلى GitHub
git remote add origin https://github.com/username/repository-name.git
git push -u origin main
```

#### 2. ربط Vercel بـ GitHub
1. اذهب إلى [Vercel Dashboard](https://vercel.com/dashboard)
2. اضغط على "New Project"
3. اختر "Import Git Repository"
4. اختر repository الخاص بك
5. اضغط "Import"

#### 3. تكوين المشروع
- **Framework Preset**: اختر "Other"
- **Root Directory**: اتركه فارغاً (./)
- **Build Command**: اتركه فارغاً
- **Output Directory**: اتركه فارغاً
- **Install Command**: `pip install -r requirements.txt`

#### 4. النشر
- اضغط "Deploy"
- انتظر حتى يكتمل البناء والنشر

### الطريقة الثانية: النشر عبر Vercel CLI

#### 1. تثبيت Vercel CLI
```bash
npm install -g vercel
```

#### 2. تسجيل الدخول
```bash
vercel login
```

#### 3. النشر
```bash
vercel
```

#### 4. متابعة التعليمات
- اختر "Link to existing project" أو "Create new project"
- اتبع التعليمات على الشاشة

## إعدادات مهمة

### متغيرات البيئة (Environment Variables)
في Vercel Dashboard، أضف المتغيرات التالية:
```
FLASK_ENV=production
VERCEL_ENV=true
```

### إعدادات البناء
تأكد من أن ملف `vercel.json` يحتوي على الإعدادات الصحيحة:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

## حل المشاكل الشائعة

### مشكلة: "Module not found"
**الحل**: تأكد من أن جميع المكتبات موجودة في `requirements.txt`

### مشكلة: "Database connection error"
**الحل**: هذا طبيعي في Vercel لأن قاعدة البيانات في الذاكرة. البيانات ستختفي عند إعادة تشغيل الخدمة.

### مشكلة: "Static files not found"
**الحل**: تأكد من وجود مجلد `static` وملف `style.css`

### مشكلة: "Model file not found"
**الحل**: تأكد من أن ملف `best_loan_model.joblib` موجود في المجلد الجذر

## اختبار التطبيق

### بعد النشر
1. اذهب إلى URL المقدم من Vercel
2. اختبر جميع الصفحات:
   - الصفحة الرئيسية
   - إضافة طلب جديد
   - عرض الطلبات
   - تحليل البيانات
   - مقاييس النموذج

### اختبار محلي قبل النشر
```bash
# تشغيل التطبيق المحلي
python flask_app.py

# أو تشغيل نسخة Vercel
python api/index.py
```

## تحديث التطبيق

### عبر GitHub
1. احدث الكود محلياً
2. ارفع التحديثات إلى GitHub
3. Vercel سيقوم بالنشر التلقائي

### عبر Vercel CLI
```bash
vercel --prod
```

## مراقبة الأداء

### في Vercel Dashboard
- اذهب إلى "Functions" لمراقبة استدعاءات API
- اذهب إلى "Analytics" لمراقبة الأداء
- اذهب إلى "Logs" لمراقبة الأخطاء

### إعدادات المراقبة
```bash
# مراقبة Logs في الوقت الفعلي
vercel logs --follow
```

## نصائح مهمة

1. **قاعدة البيانات**: استخدم قاعدة بيانات خارجية للإنتاج (مثل PostgreSQL)
2. **الملفات الكبيرة**: تجنب رفع ملفات كبيرة (>50MB)
3. **الذاكرة**: Vercel محدود بـ 1024MB ذاكرة
4. **الوقت**: كل function محدودة بـ 10 ثوانٍ (يمكن زيادتها إلى 30)

## الدعم
- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Flask on Vercel](https://vercel.com/guides/deploying-flask-with-vercel)

## مثال على URL النهائي
```
https://your-project-name.vercel.app
``` 