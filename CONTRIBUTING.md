# دليل المساهمة | Contributing Guide

شكراً لاهتمامك بالمساهمة في موسوعة الذكاء الاصطناعي العربي! هذا الدليل يساعدك على فهم كيفية المساهمة الفعالة.

Thank you for your interest in contributing to Awesome Arabic AI! This guide will help you contribute effectively.

---

## 🎯 أهدافنا | Our Goals

موسوعة الذكاء الاصطناعي العربي تهدف إلى أن تكون:

- **الأشمل**: تغطية شاملة لموارد الذكاء الاصطناعي العربية
- **الأدق**: معلومات دقيقة ومحدثة عن كل مورد
- **الأسهل**: تنظيم واضح وسهل البحث
- **الأكثر فائدة**: موارد فعلاً مفيدة وعملية

This awesome list aims to be:
- **Comprehensive**: Complete coverage of Arabic AI resources
- **Accurate**: Up-to-date and verified information
- **Organized**: Clear, searchable structure
- **Useful**: Genuinely practical resources

---

## ✅ معايير الجودة | Quality Criteria

قبل إضافة أي مورد، تأكد من توفر المعايير التالية:

Before adding any resource, ensure it meets these criteria:

### المعايير الأساسية | Core Criteria

1. **الصلة بالموضوع** | Relevance
   - ✅ المورد يتعلق مباشرة بالذكاء الاصطناعي والعربية
   - ✅ The resource is directly related to AI and Arabic language

2. **الفعالية** | Active Maintenance
   - ✅ المشروع نشط ومدعوم بشكل مستمر
   - ✅ Project is actively maintained and updated
   - ✅ آخر تحديث خلال السنة الماضية (على الأقل)
   - ✅ Last update within the past year (minimum)

3. **الإتاحة العامة** | Public Access
   - ✅ المورد متاح للعامة دون تسجيل دخول إجباري أو صلاحيات خاصة
   - ✅ Resource is publicly accessible without mandatory login or special permissions

4. **الوضوح** | Clear Documentation
   - ✅ المورد له وثائق واضحة ومفيدة
   - ✅ The resource has clear, helpful documentation
   - ✅ سهل الفهم والاستخدام
   - ✅ Easy to understand and use

5. **الدقة** | Accuracy
   - ✅ المعلومات المقدمة صحيحة وموثوقة
   - ✅ Information is accurate and verifiable
   - ✅ الأوصاف تعكس المورد بشكل صحيح
   - ✅ Description accurately reflects the resource

6. **البدائل** | Uniqueness
   - ✅ المورد يقدم شيئاً جديداً أو مختلفاً
   - ✅ The resource offers something new or different
   - ✅ لا يكون نسخة مطابقة تماماً من مورد موجود
   - ✅ Not a duplicate of an existing resource

---

## 📝 كيفية المساهمة | How to Contribute

### الخطوة 1: Fork المشروع

```bash
# انسخ المشروع إلى حسابك
git clone https://github.com/azizalzahrani/awesome-arabic-ai.git
cd awesome-arabic-ai
```

### الخطوة 2: أنشئ فرع عمل

```bash
# أنشئ فرع جديد للمورد الذي تريد إضافته
git checkout -b add/new-resource-name
# أو للتحسينات
git checkout -b improve/description
```

### الخطوة 3: أضف المورد

اتبع القالب الموضح أدناه بدقة.

### الخطوة 4: اختبر وتحقق

- ✅ تحقق من صحة الروابط
- ✅ تأكد من التنسيق الصحيح
- ✅ اقرأ النص للتأكد من الأخطاء الإملائية

### الخطوة 5: ارفع التغييرات

```bash
git add README.md
git commit -m "feat: إضافة مورد جديد - اسم المورد"
# أو بالإنجليزية
git commit -m "feat: Add new resource - resource-name"
git push origin add/new-resource-name
```

### الخطوة 6: افتح Pull Request

- اشرح ماذا أضفت وماذا يقدم المورد
- تأكد من أن PR يشير إلى أي issue ذي صلة

---

## 📋 قوالب الإضافة | Submission Templates

### قالب: إضافة نموذج لغة جديد | LLM Template

```markdown
| **[اسم النموذج](رابط-github)** | [الجهة المطورة] | [الحجم] | [رابط-huggingface] | وصف موجز بالعربية عن النموذج ومميزاته | Brief English description |
```

**مثال:**
```markdown
| **CustomAI** | Example Inc. | 13B | [huggingface.co/example/custom](https://huggingface.co/example/custom) | نموذج عربي متخصص في المحتوى الإخباري | Arabic model specialized in news content |
```

### قالب: إضافة مجموعة بيانات | Dataset Template

```markdown
| **[اسم المجموعة](رابط)** | [الحجم] | [المهمة] | [رابط-اخر] | وصف المجموعة بالعربية | English description |
```

**مثال:**
```markdown
| **NewsCorpus** | 500K docs | Text Classification | [github.com/example/newscorpus](https://github.com) | مجموعة أخبار عربية موسومة للتصنيف | Labeled Arabic news corpus for classification |
```

### قالب: إضافة أداة | Tool Template

```markdown
| **[اسم الأداة](رابط)** | [الغرض الرئيسي] | [رابط-github] | وصف الأداة بالعربية | English description |
```

**مثال:**
```markdown
| **TextAnalyzer** | تحليل نصي | [github.com/example/analyzer](https://github.com) | أداة لتحليل النصوص العربية والإحصائيات | Tool for analyzing Arabic text and statistics |
```

### قالب: إضافة ورقة بحثية | Paper Template

```markdown
| **[عنوان الورقة](رابط-arxiv)** | [الجهة] | [السنة] | [رابط-pdf] | ملخص الورقة بالعربية | English abstract |
```

**مثال:**
```markdown
| **Arabic NLP: Modern Approaches** | University X | 2024 | [arxiv.org/abs/2401.xxxxx](https://arxiv.org) | دراسة حول أحدث تقنيات معالجة اللغة العربية | Study on modern Arabic NLP techniques |
```

### قالب: إضافة شركة | Company Template

```markdown
| **[اسم الشركة](رابط)** | 🇸🇦 [البلد] | [التخصص] | [الرابط] | وصف الشركة ومجالات عملها | Company description and focus areas |
```

**مثال:**
```markdown
| **AI Solutions Inc.** | 🇸🇦 السعودية | تطبيقات ذكاء اصطناعي | [example.com](https://example.com) | شركة متخصصة في تطوير تطبيقات الذكاء الاصطناعي للقطاع الخاص | Company specializing in AI applications for private sector |
```

---

## 🔍 نصائح عملية | Practical Tips

### التحقق من الروابط

تأكد من أن كل رابط يعمل بشكل صحيح:

```bash
# استخدم أداة مثل curl للتحقق
curl -I https://example.com
```

### الأوصاف باللغة العربية

- استخدم لغة واضحة وبسيطة
- تجنب الأخطاء الإملائية والنحوية
- اكتب جملاً قصيرة وواضحة
- استخدم الخط العربي الصحيح (نص عادي، لا صور)

**Tips for Arabic descriptions:**
- Use clear, simple language
- Avoid spelling and grammar mistakes
- Write short, clear sentences
- Use proper Arabic script (text, not images)

### التنسيق والترتيب

- رتب الموارد حسب الأهمية والشهرة
- استخدم الأيقونات (emoji) بشكل متسق
- اتبع الترتيب الموجود في الملف
- تأكد من توازن الجداول

### الأيقونات الموصى بها

- 🌟 نجمة: نماذج/موارد موصى بها
- 🔍 عدسة: أبحاث وأوراق علمية
- 📊 رسم بياني: بيانات وإحصائيات
- 🛠️ مفتاح: أدوات وتطبيقات
- 🏛️ مبنى: شركات ومؤسسات
- 📚 كتاب: دورات وموارد تعليمية
- 🎤 ميكرفون: مجتمعات وفعاليات

---

## 🚫 ماذا لا تفعل | What NOT to Do

لا تضف مشاريع/موارد إذا:

❌ **المشروع غير نشط**: لم يتم التحديث لأكثر من سنة
❌ **الروابط معطلة**: الموقع غير متاح أو الرابط خاطئ
❌ **مكرر تماماً**: نسخة مطابقة من مورد موجود بالفعل
❌ **محتوى سيء**: التوثيق ضعيف أو غير واضح
❌ **غير صلة**: لا علاقة بالذكاء الاصطناعي أو العربية
❌ **غير متاح للعامة**: يتطلب تسجيل دخول إجباري أو صلاحيات خاصة
❌ **ترويج ذاتي**: تضيف فقط لتروج منتجك الخاص

Do NOT add projects/resources if:

❌ **Inactive**: Not updated for more than a year
❌ **Broken links**: Website unavailable or wrong URL
❌ **Exact duplicate**: Already exists in the list
❌ **Poor quality**: Weak or unclear documentation
❌ **Not relevant**: Not related to AI or Arabic
❌ **Not publicly accessible**: Requires mandatory login or special permissions
❌ **Self-promotion only**: Adding just to promote your product

---

## 💬 كيفية الحصول على الدعم | Getting Help

إذا كان لديك أسئلة:

- **افتح Issue**: اشرح سؤالك بوضوح
- **ناقش أولاً**: اطلب رأي الفريق قبل إضافة موارد كبيرة
- **استشر المساهمين**: تواصل مع المساهمين الآخرين

If you have questions:
- **Open an Issue**: Describe your question clearly
- **Discuss First**: Ask for team feedback before adding major resources
- **Consult Contributors**: Reach out to other contributors

---

## 📊 قائمة فحص قبل الإرسال | Pre-Submission Checklist

قبل إرسال PR، تحقق من:

Before submitting a PR, check:

- [ ] ✅ النص العربي صحيح وواضح (Arabic text is correct and clear)
- [ ] ✅ جميع الروابط تعمل بشكل صحيح (All links work correctly)
- [ ] ✅ المورد متوافق مع معايير الجودة (Resource meets quality criteria)
- [ ] ✅ التنسيق يتبع القالب الموجود (Format follows existing template)
- [ ] ✅ لا توجد أخطاء إملائية (No spelling mistakes)
- [ ] ✅ المورد ليس مكرراً (Resource is not a duplicate)
- [ ] ✅ المورد متاح للعامة بدون وصول خاص (Resource is publicly accessible)
- [ ] ✅ الوصف دقيق وصحيح (Description is accurate)
- [ ] ✅ رسالة الـ commit واضحة (Commit message is clear)

---

## 🎓 أمثلة على مساهمات ممتازة | Examples of Great Contributions

### مثال 1: إضافة نموذج جديد

```markdown
| **MARBERTv2** | UBC-NLP | Base | [huggingface.co/UBC-NLP/MARBERTv2](https://huggingface.co/UBC-NLP/MARBERTv2) | نموذج Transformer عربي قوي للهجات العربية والنصوص الاجتماعية | Strong Arabic transformer model for dialects and social text |
```

### مثال 2: إضافة مجموعة بيانات

```markdown
| **Arabic Legal Dataset** | 150K docs | Classification | [github.com/example/legal-dataset](https://github.com/example/legal-dataset) | مجموعة شاملة من النصوص القانونية العربية للتصنيف والتحليل | Comprehensive Arabic legal texts for classification and analysis |
```

### مثال 3: تحسين وصف موجود

```
قبل: أداة معالجة النصوص
بعد: أداة معالجة النصوص العربية المتقدمة مع دعم التحليل الصرفي واستخراج الجذور
```

---

## 📞 التواصل | Contact

- **GitHub Issues**: للأسئلة والنقاش
- **Pull Requests**: للمساهمات المباشرة
- **Email**: يمكن الاتصال عبر البيانات الموجودة في ملف Profile

---

## 🙏 شكراً | Thank You

شكراً على مساهمتك في جعل موسوعة الذكاء الاصطناعي العربي أفضل!

Thank you for helping make Awesome Arabic AI better!

**جميع المساهمين الكرام - Thank you to all our contributors!**

---

*آخر تحديث: 2026-03-23*
*Last Updated: 2026-03-23*
