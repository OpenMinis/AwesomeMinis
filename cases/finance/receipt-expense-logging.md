# Photo a Receipt → Auto-Log Expense

> 💬 *From **Zigzag** · 2026-03-30 (via DM)*

---

## 🎯 Pain Point

Manual expense logging after shopping is a chore: open the app, enter merchant, amount, category, date… You skip it every time, and your finances stay a mess.

---

## 💡 What It Does

Take a shopping receipt and send it to Minis. It calls Apple Vision to identify the content of the receipt, extract the merchant name, total amount, product details, consumption time, automatically classify it (shopping/dining/transportation, etc.), complete accounting and output a structured bill.

Actual measurement results (Hema fresh receipts):
- ✅ Correctly identify the merchant: Hema
- ✅ Amount: ¥82.60 (7 items)
- ✅Automatic classification: shopping
- ✅ Identify discounted products and get accurate prices after discounts
- 💡 Use Apple Vision local recognition, no need to connect to the Internet, accurate recognition in dark light environment with normal lights on.

Take a photo of a receipt and send it to Minis. It uses Apple Vision to OCR the receipt, extracts merchant name, total amount, item breakdown, and timestamp, auto-categorizes the expense (shopping/dining/transport, etc.), and outputs a structured expense record.

Real test (Hema Fresh receipt):
- ✅ Merchant: Hema Fresh
- ✅ Amount: ¥82.60 (7 items)
- ✅ Auto-category: Shopping
- ✅ Correctly identified discounted items with final price
- 💡 Uses Apple Vision for local OCR — no network needed, works well under normal indoor lighting

---

## 🛠 Skills Used

| Skill | Purpose |
|-------|---------|
| Built-in Apple Vision | Run local receipt OCR |
| Built-in shell | Parse the OCR result and generate an expense log |

---

## 💬 Example Prompt


```
(Attach receipt photo)
Log this expense for me.
```

---

## 📸 Screenshots

![Screenshot by Zigzag](../../assets/screenshots/receipt-expense-logging.jpg)

*📷 Shared by **Zigzag** · 2026-03-30 — Take Hema fresh receipts, automatically identify 7 product details, total ¥82.60, classified as shopping*

---

## ⚙️ Requirements

- [ ] No additional configuration required, Apple Vision is a built-in capability
- [ ] It is recommended to shoot under normal indoor light and avoid strong reflections.

---

## 💡 Tips

- Support receipts containing discounted products, and the discounted price can be accurately identified
- You can ask Minis to append accounting data to a CSV file, and perform monthly analysis after long-term accumulation.
- You can also directly take screenshots of takeout orders, the effect is equally accurate

---

## 👤 Contributor

From the Open Minis Telegram community

Original sharer: **Zigzag**

---

## 📅 Last Verified

2026-03-30
