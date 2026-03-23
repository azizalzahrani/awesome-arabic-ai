# موسوعة الذكاء الاصطناعي العربي 🌟
# Awesome Arabic AI

> أكبر مجموعة مُنسّقة لموارد الذكاء الاصطناعي العربية
> The largest curated collection of Arabic AI resources

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0 1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--03--23-blue)

> تم التحقق يدوياً من الروابط العامة في هذه القائمة بتاريخ 2026-03-23.
> Public links in this list were manually verified on 2026-03-23.

---

## المحتويات | Contents

- [نماذج اللغة العربية](#نماذج-اللغة-العربية--arabic-language-models) | [Arabic Language Models](#نماذج-اللغة-العربية--arabic-language-models)
- [مجموعات البيانات](#مجموعات-البيانات--datasets) | [Datasets](#مجموعات-البيانات--datasets)
- [أدوات معالجة اللغة الطبيعية](#أدوات-معالجة-اللغة-الطبيعية--arabic-nlp-tools) | [Arabic NLP Tools](#أدوات-معالجة-اللغة-الطبيعية--arabic-nlp-tools)
- [مشاريعنا المفتوحة](#مشاريعنا-المفتوحة--our-open-source-projects-) | [Our Open Source Projects](#مشاريعنا-المفتوحة--our-open-source-projects-)
- [الأبحاث والأوراق العلمية](#الأبحاث-والأوراق-العلمية--research-papers) | [Research Papers](#الأبحاث-والأوراق-العلمية--research-papers)
- [الشركات العربية](#الشركات-العربية-في-الذكاء-الاصطناعي--arab-ai-companies) | [Arab AI Companies](#الشركات-العربية-في-الذكاء-الاصطناعي--arab-ai-companies)
- [المجتمعات والمنتديات](#المجتمعات-والمنتديات--communities) | [Communities](#المجتمعات-والمنتديات--communities)
- [الدورات التعليمية](#الدورات-التعليمية--courses--tutorials) | [Courses & Tutorials](#الدورات-التعليمية--courses--tutorials)
- [مطورون عرب مؤثرون](#مطورون-عرب-مؤثرون--notable-arab-ai-developers) | [Notable Arab AI Developers](#مطورون-عرب-مؤثرون--notable-arab-ai-developers)
- [المساهمة](#المساهمة--contributing) | [Contributing](#المساهمة--contributing)

---

## نماذج اللغة العربية | Arabic Language Models

### Large Language Models (LLMs)

| النموذج | الجهة | الحجم | الرابط | الوصف |
|---------|------|------|--------|--------|
| **Jais** | Inception / Core42 | 13B/30B | [huggingface.co/inceptionai/jais-13b-chat](https://huggingface.co/inceptionai/jais-13b-chat) | نموذج عربي-إنجليزي عالي الأداء من الإمارات، مُحسّن لفهم وتوليد اللغة العربية |
| **ALLaM** | HUMAIN | 7B | [huggingface.co/humain-ai/ALLaM-7B-Instruct-preview](https://huggingface.co/humain-ai/ALLaM-7B-Instruct-preview) | نموذج تعليماتي عربي متاح كمعاينة عامة، موجّه للحوار والمهام العربية |
| **Falcon** | TII | 7B/40B | [falconllm.tii.ae](https://falconllm.tii.ae/) | نموذج مفتوح المصدر من معهد تقنية الابتكار بالإمارات، يدعم العربية ضمن عائلة نماذج متعددة اللغات |
| **Qwen** | Alibaba | 1B-110B | [huggingface.co/Qwen](https://huggingface.co/Qwen) | نموذج صيني متعدد اللغات بدعم قوي للعربية |
| **BLOOM** | BigScience | 176B | [huggingface.co/bigscience/bloom](https://huggingface.co/bigscience/bloom) | نموذج متعدد اللغات يشمل العربية، مفتوح المصدر |
| **AceGPT** | Freedom Intelligence | 7B/13B | [huggingface.co/FreedomIntelligence/AceGPT-7B-chat](https://huggingface.co/FreedomIntelligence/AceGPT-7B-chat) | نموذج متعدد اللغات مع إصدارات عامة تدعم العربية ومهام المحادثة |

### Arabic BERT & Transformer Models

| النموذج | الجهة | الرابط | الوصف |
|---------|------|--------|--------|
| **AraBERT** | AUB CAMEL | [huggingface.co/aubmindlab/bert-base-arabertv2](https://huggingface.co/aubmindlab/bert-base-arabertv2) | نموذج BERT مُدرَّب مسبقاً للعربية من جامعة الأمريكية في بيروت |
| **MARBERTv2** | UBC-NLP | [huggingface.co/UBC-NLP/MARBERTv2](https://huggingface.co/UBC-NLP/MARBERTv2) | نموذج Transformer عربي قوي للهجات العربية والنصوص الاجتماعية |
| **CAMeLBERT** | CAMeL Lab | [huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix) | عائلة نماذج BERT عربية تدعم الفصحى واللهجات ومهام التصنيف المختلفة |
| **mBERT** | Google | [huggingface.co/google-bert/bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased) | BERT متعدد اللغات يشمل العربية |
| **XLM-RoBERTa** | Facebook | [huggingface.co/FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) | نموذج RoBERTa متعدد اللغات يدعم العربية |

### Embedding Models

| النموذج | الرابط | الوصف |
|---------|--------|--------|
| **multilingual-e5-base** | [huggingface.co/intfloat/multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) | نموذج Embeddings متعدد اللغات مناسب للاسترجاع والبحث الدلالي ويدعم العربية |
| **paraphrase-multilingual-mpnet-base-v2** | [huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) | نموذج تمثيل متعدد اللغات مفيد للتشابه الدلالي وتجميع النصوص العربية |

---

## مجموعات البيانات | Datasets

### Text Corpora

| المجموعة | الحجم | الاستخدام | الرابط | الوصف |
|---------|------|----------|--------|--------|
| **OSCAR (Arabic)** | ~77GB | Pre-training | [huggingface.co/datasets/oscar](https://huggingface.co/datasets/oscar) | مجموعة نصوص عربية ضخمة مستخرجة من الويب، مشروع مفتوح المصدر |
| **Arabic Wikipedia** | ~200MB | Reference | [dumps.wikimedia.org](https://dumps.wikimedia.org/arwiki/) | صفحات الموسوعة الحرة العربية، نصوص عالية الجودة |
| **OpenITI** | ~25B words | Historical texts | [openiti.org](https://openiti.org) | مشروع الكتب الإسلامية والعربية مفتوحة المصدر |
| **Arabic Gigaword** | 900K docs | News | [catalog.ldc.upenn.edu](https://catalog.ldc.upenn.edu/LDC2011T11) | مجموعة ضخمة من الأخبار العربية |

### Task-Specific Datasets

| المجموعة | المهمة | الحجم | الرابط | الوصف |
|---------|------|------|--------|--------|
| **ARCD** | Reading Comprehension | 1.4K QA pairs | [huggingface.co/datasets/arcd](https://huggingface.co/datasets/arcd) | مجموعة اختبار قراءة الفهم العربية |
| **Tashkeela** | Diacritization | 400K+ words | [huggingface.co/datasets/arbml/tashkeela](https://huggingface.co/datasets/arbml/tashkeela) | مجموعة نصوص عربية مشكلة (بالحركات) |
| **Arabic Web Treebank** | Parsing | 30K sentences | [universaldependencies.org/treebanks/ar_padt](https://universaldependencies.org/treebanks/ar_padt/index.html) | مجموعة جمل عربية موسومة بشجرة التحليل |

---

## أدوات معالجة اللغة الطبيعية | Arabic NLP Tools

### Comprehensive NLP Frameworks

| الأداة | الغرض الرئيسي | الرابط | الوصف |
|------|-------------|--------|--------|
| **CAMeL Tools** | شاملة | [github.com/CAMeL-Lab/CAMeL_Tools](https://github.com/CAMeL-Lab/CAMeL_Tools) | مجموعة شاملة من أدوات معالجة اللغة الطبيعية العربية: تحليل صرفي، التعرف على اللهجات، الترقيم |
| **Farasa** | شاملة | [farasa.qcri.org](https://farasa.qcri.org/) | أداة معالجة نصوص عربية قوية مع دعم التحليل الصرفي والجذر |
| **Madamira** | تحليل صرفي | [camel.abudhabi.nyu.edu/madamira/](https://camel.abudhabi.nyu.edu/madamira/) | نظام تحليل صرفي متقدم للعربية |
| **Stanza (Arabic)** | شاملة | [stanfordnlp.github.io/stanza/](https://stanfordnlp.github.io/stanza/) | مكتبة معالجة لغة طبيعية من Stanford مع دعم العربية |
| **spaCy (Arabic models)** | شاملة | [spacy.io](https://spacy.io) | مكتبة NLP حديثة مع نماذج عربية |

### Text Processing Utilities

| الأداة | الوظيفة | الرابط | الوصف |
|------|--------|--------|--------|
| **PyArabic** | معالجة عامة | [github.com/linuxscout/pyarabic](https://github.com/linuxscout/pyarabic) | مكتبة Python لمعالجة النصوص العربية |
| **Arabic Reshaper** | تشكيل النص | [github.com/mpcabd/python-arabic-reshaper](https://github.com/mpcabd/python-arabic-reshaper) | أداة لتشكيل النصوص العربية للعرض الصحيح |
| **Python-bidi** | النصوص ثنائية الاتجاه | [github.com/MeirKriheli/python-bidi](https://github.com/MeirKriheli/python-bidi) | معالجة النصوص من اليمين إلى اليسار |
| **AraBERT Preprocessing** | معالجة مسبقة | [github.com/aub-mind/arabert](https://github.com/aub-mind/arabert) | أدوات معالجة مسبقة متخصصة للعربية |

### Specialized Tools

| الأداة | التخصص | الرابط | الوصف |
|------|--------|--------|--------|
| **Farasapy** | Tokenization & Segmentation | [github.com/MagedSaeed/farasapy](https://github.com/MagedSaeed/farasapy) | واجهة Python لخدمة Farasa تدعم التقسيم والتجزئة النصية للعربية |
| **ArabicSpellChecker** | التحقق الإملائي | [github.com/qcri/ArabicSpellChecker](https://github.com/qcri/ArabicSpellChecker) | أداة للتحقق من الأخطاء الإملائية في النصوص العربية |

---

## مشاريعنا المفتوحة | Our Open Source Projects ⭐

**تطوير مجموعة متكاملة من الأدوات المتخصصة لمعالجة اللغة العربية في عصر الذكاء الاصطناعي**

| المشروع | الوصف | الرابط |
|--------|------|--------|
| **arabic-rag-toolkit** 🔍 | مجموعة أدوات استرجاع المعلومات وتوليد الإجابات (RAG) المتخصصة للعربية، مع دعم الأنماط الحديثة والتكامل السلس مع نماذج اللغة | [github.com/azizalzahrani/arabic-rag-toolkit](https://github.com/azizalzahrani/arabic-rag-toolkit) |
| **arabic-content-moderation** 🛡️ | نظام ذكي لمراقبة وتصنيف المحتوى العربي، يكشف المحتوى الضار والعنف واللغة البذيئة | [github.com/azizalzahrani/arabic-content-moderation](https://github.com/azizalzahrani/arabic-content-moderation) |
| **arabic-docs-translator** 📚 | أداة متخصصة في ترجمة التوثيقات التقنية من الإنجليزية إلى العربية مع الحفاظ على الصيغة والتنسيق | [github.com/azizalzahrani/arabic-docs-translator](https://github.com/azizalzahrani/arabic-docs-translator) |

---

## الأبحاث والأوراق العلمية | Research Papers

### Recent Papers (2023-2026)

| الورقة | الجهة | السنة | الرابط | الملخص |
|-------|------|------|--------|--------|
| **Jais: A Fully Arabic-Centric LLM** | Inception/G42 | 2023 | [arxiv.org/abs/2308.16149](https://arxiv.org/abs/2308.16149) | أول نموذج لغة عربي-إنجليزي متوازن كبير الحجم |
| **AraBERT: Transformer-based Model for Arabic Language Understanding** | AUB | 2020 | [arxiv.org/abs/2003.00104](https://arxiv.org/abs/2003.00104) | نموذج BERT متقدم للفهم العميق للغة العربية |
| **Modern Arabic NLP: A Comprehensive Survey** | Multiple | 2022 | [arxiv.org/abs/2210.05444](https://arxiv.org/abs/2210.05444) | مسح شامل لأحدث تقنيات معالجة اللغة الطبيعية العربية |
| **Curated Corpora for Automatic Arabic Dialect Detection** | KAUST | 2021 | [arxiv.org/abs/2109.14948](https://arxiv.org/abs/2109.14948) | دراسة عميقة في التعرف على اللهجات العربية |
| **Falcon: A Language Model for Open Domain Reasoning** | TII | 2023 | [arxiv.org/abs/2311.16867](https://arxiv.org/abs/2311.16867) | نموذج لغة متقدم مع دعم قوي للعربية |

### Benchmark & Evaluation Papers

| الورقة | الرابط | الوصف |
|-------|--------|--------|
| **ALUE: Arabic Language Understanding Evaluation** | [arxiv.org/abs/2101.10012](https://arxiv.org/abs/2101.10012) | معايير تقييم موحدة للغة العربية |
| **Arabic Named Entity Recognition: A Literature Review** | [arxiv.org/abs/2104.10255](https://arxiv.org/abs/2104.10255) | مراجعة شاملة لأبحاث التعرف على الكيانات المسماة |

---

## الشركات العربية في الذكاء الاصطناعي | Arab AI Companies

### حكومية ومؤسسات وطنية

| الشركة | الدولة | التخصص | الرابط | الوصف |
|-------|-------|--------|--------|--------|
| **SDAIA** | 🇸🇦 السعودية | ذكاء اصطناعي وطني | [sdaia.gov.sa](https://sdaia.gov.sa) | الهيئة السعودية للبيانات والذكاء الاصطناعي، تطور ALLaM ومبادرات وطنية |
| **TII** | 🇦🇪 الإمارات | التكنولوجيا المتقدمة | [tii.ae](https://tii.ae) | معهد تقنية الابتكار، طور نموذج Falcon المفتوح المصدر |
| **G42** | 🇦🇪 الإمارات | الحوسبة السحابية والذكاء الاصطناعي | [g42.ai](https://g42.ai) | شركة رائدة في الذكاء الاصطناعي والحوسبة السحابية بالشرق الأوسط |

### شركات خاصة ناشئة

| الشركة | الدولة | التخصص | الرابط | الوصف |
|-------|-------|--------|--------|--------|
| **Mozn** | 🇸🇦 السعودية | حلول ذكاء اصطناعي | [mozn.ai](https://mozn.ai) | متخصصة في تطبيقات الذكاء الاصطناعي للقطاع الخاص |
| **Lucidya** | 🇸🇦 السعودية | تحليل وسائل التواصل | [lucidya.com](https://lucidya.com) | منصة تحليل المشاعر والوسائط الاجتماعية العربية |
| **Lean Technologies** | 🇸🇦 السعودية | التكنولوجيا المالية | [lean.technology](https://lean.technology) | منصة البنوك المفتوحة الرائدة |
| **Elm** | 🇸🇦 السعودية | الحلول الرقمية | [elm.sa](https://elm.sa) | متخصصة في التحول الرقمي والحلول الذكية |

### الشركات الكبرى مع مبادرات ذكاء اصطناعي

| الشركة | الدولة | المبادرات | الرابط |
|-------|-------|----------|--------|
| **STC** | 🇸🇦 السعودية | 5G، IoT، وحلول ذكية | [stc.com.sa](https://stc.com.sa) |
| **Careem** | 🇦🇪/🇸🇦 الإمارات/السعودية | تطبيقات الذكاء الاصطناعي في خدمات التنقل | [careem.com](https://careem.com) |

---

## المجتمعات والمنتديات | Communities

### Online Communities & Networks

| المجتمع | المنصة | الوصف | الرابط |
|--------|--------|--------|--------|
| **CAMeL Lab** | Website | مختبر وأرشيف أبحاث وموارد متخصص في اللغة العربية ومعالجة اللهجات | [camel.abudhabi.nyu.edu](https://camel.abudhabi.nyu.edu/) |
| **Hugging Face Forums (Arabic NLP)** | Forum | نقاشات وأسئلة حول النماذج والأدوات العربية على منصة Hugging Face | [discuss.huggingface.co/search?q=arabic%20nlp](https://discuss.huggingface.co/search?q=arabic%20nlp) |

### Conferences & Events

| الحدث | التكرار | الموقع | الوصف |
|------|--------|--------|--------|
| **ArabAI Summit** | سنوي | الخليج | مؤتمر سنوي لأحدث تطورات الذكاء الاصطناعي في الوطن العربي |
| **Arabic NLP Workshop** | مختلف | متنوع | ورش عمل متخصصة في معالجة اللغة الطبيعية العربية |

### Influential Accounts to Follow

**على منصات التواصل (X/Twitter, LinkedIn):**
- **@az_zahrani** - مصدر معلومات متخصص في الذكاء الاصطناعي العربي
- **@SDAIA_SA** - التحديثات الرسمية من الهيئة السعودية للبيانات والذكاء الاصطناعي
- **@TII_AE** - أخبار ومنشورات معهد تقنية الابتكار
- **@CAMeL_Lab** - أبحاث ومشاريع معهد NYU Abu Dhabi
- **@ArabicNLP** - أحدث الدراسات والأدوات في معالجة اللغة العربية

---

## الدورات التعليمية | Courses & Tutorials

### الدورات الأكاديمية

| الدورة | الجهة | المستوى | الرابط | الوصف |
|-------|------|--------|--------|--------|
| **CS224N: NLP with Deep Learning** | Stanford | متقدم | [cs224n.stanford.edu](https://cs224n.stanford.edu) | دورة معروفة عالمياً مع موارد خاصة للعربية |
| **Hugging Face LLM Course** | Hugging Face | متوسط | [huggingface.co/learn/nlp-course/](https://huggingface.co/learn/nlp-course/) | دورة مجانية حديثة لفهم النماذج اللغوية ويمكن تطبيق مفاهيمها على العربية |
| **Practical Deep Learning for Coders** | Fast.ai | متوسط | [course.fast.ai](https://course.fast.ai/) | دورة عملية لتطبيق أساليب التعلم العميق وNLP على بيانات متعددة اللغات |

### البرامج والأكاديميات السعودية

| البرنامج | الجهة | النوع | الرابط | الوصف |
|---------|------|------|--------|--------|
| **Tuwaiq Academy** | SDAIA | مكثف | [tuwaiq.edu.sa](https://tuwaiq.edu.sa/) | أكاديمية متخصصة في برامج البرمجة والذكاء الاصطناعي |
| **SDAIA Academy** | SDAIA | متنوع | [sdaia.gov.sa](https://sdaia.gov.sa) | برامج تدريبية متقدمة في الذكاء الاصطناعي |

### مصادر تعليمية مفتوحة

| المورد | نوعه | الرابط | الوصف |
|--------|------|--------|--------|
| **CAMeL Tools Tutorial** | فيديو/نصي | [github.com/CAMeL-Lab/CAMeL_Tools](https://github.com/CAMeL-Lab/CAMeL_Tools) | شروحات عملية لاستخدام أدوات CAMeL |
| **Arabic BERT Guide** | مقالات | [huggingface.co/aubmindlab](https://huggingface.co/aubmindlab) | دليل شامل لاستخدام AraBERT |

---

## مطورون عرب مؤثرون | Notable Arab AI Developers

| المطور | الاهتمام الرئيسي | المنصة | الوصف |
|--------|------------------|--------|--------|
| **Aziz Al-Zahrani** | RAG، معالجة النصوص | GitHub/Twitter | محترف متخصص في تطوير أدوات الذكاء الاصطناعي للغة العربية |
| **Nizar Habash** | معالجة اللغة الطبيعية | NYU Abu Dhabi | باحث رائد في تقنيات معالجة اللغة العربية |
| **Tamer Elsayed** | البحث والاسترجاع | Qatar University | متخصص في استرجاع المعلومات والبحث العربي |
| **Salim Roukos** | ترجمة آلية | IBM Research | خبير في الترجمة الآلية ومعالجة اللغات متعددة |

---

## المساهمة | Contributing

شكراً لاهتمامك بالمساهمة في هذا المشروع! نرحب بإضافة موارد جديدة وتحسينات.

**Thank you for your interest in contributing! We welcome new resources and improvements.**

### شروط الجودة | Quality Criteria

قبل تقديم طلب دمج (PR)، تأكد من أن المورد يحقق المعايير التالية:

Before submitting a PR, ensure your resource meets these criteria:

- ✅ **متاح ومعمول به** | Active and maintained
- ✅ **ذو علاقة بالذكاء الاصطناعي العربي** | Related to Arabic AI
- ✅ **وصف دقيق وواضح** | Accurate, clear description
- ✅ **لينك صحيح وعامل** | Valid, working link
- ✅ **متاح للعامة** | Publicly accessible without required login
- ✅ **بدون محتوى مكرر** | No duplicates

### كيفية المساهمة | How to Contribute

1. **Fork** المشروع
2. أنشئ فرع جديد: `git checkout -b add-awesome-resource`
3. أضف المورد مع وصف عربي وإنجليزي
4. اتبع صيغة القالب أدناه
5. ارسل PR مع وصف واضح

### قالب الإضافة | Submission Template

```markdown
**Resource Name (English) | اسم المورد (عربي)**

- الرابط: [Link](https://example.com)
- الجهة: Organization Name
- الوصف: وصف موجز بالعربية | Brief description in English
- الفئة: [Models/Tools/Datasets/Papers/Companies]
- الحالة: Active/Maintained
```

### أمثلة | Examples

**مثال 1: إضافة نموذج جديد**
```
**MyArabicLLM**

- الرابط: [github.com/example/myarabicllm](https://github.com)
- الجهة: Example Organization
- الحجم: 7B parameters
- الوصف: نموذج لغة عربي بسيط للتجارب | A simple Arabic LLM for experimentation
```

**مثال 2: إضافة أداة جديدة**
```
**ArabicProcessor**

- الرابط: [github.com/example/arabic-processor](https://github.com)
- الوصف: أداة معالجة نصوص عربية متقدمة | Advanced Arabic text processing tool
- الميزات: التحليل الصرفي، استخراج الجذور | Morphological analysis, root extraction
```

### إرشادات عامة | General Guidelines

- استخدم التنسيق الموحد الموجود في الملف
- تأكد من الرابط يعمل بشكل صحيح
- أضف أيقونات/Emojis حسب الفئة
- رتب الموارد حسب الأهمية والحداثة
- اكتب الأوصاف بلغة واضحة وبسيطة

---

## الترخيص | License

هذا المشروع مرخص تحت رخصة CC0 1.0 (المجال العام)
كل المحتوى حر للاستخدام والمشاركة والتعديل.

This project is licensed under CC0 1.0 (Public Domain)
All content is free to use, share, and modify.

[رخصة كاملة | Full License](LICENSE)

---

## الإحصائيات | Statistics

- 🌍 **Languages**: العربية + English
- ⭐ **Star this Awesome List**: [github.com/azizalzahrani/awesome-arabic-ai](https://github.com/azizalzahrani/awesome-arabic-ai)
- 🔎 **Link Verification**: Manually checked on 2026-03-23
- 📊 **Last Updated**: 2026-03-23
- 👥 **Contributors**: Welcome!
- 📈 **Growth**: This list is growing continuously

---

## شكراً لك | Thank You

شكراً لاستخدامك لهذا المورد. إذا وجدت هذه القائمة مفيدة، يرجى:
- إضافة النجمة ⭐
- مشاركتها مع الآخرين
- المساهمة بموارد جديدة

Thank you for using this resource. If you find this list helpful, please:
- Star this repository ⭐
- Share it with others
- Contribute new resources

---

**صُنع بـ ❤️ بواسطة مجتمع الذكاء الاصطناعي العربي**

**Made with ❤️ by the Arabic AI Community**
