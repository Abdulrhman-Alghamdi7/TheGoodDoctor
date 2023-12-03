const { Configuration, OpenAIApi } = require("openai")
require('dotenv').config();
const express = require('express');
const ejs = require('ejs')
const app = express();
app.use(express.static('views'));
app.use(express.json());
app.set('view engine', 'ejs');

const openAi = new OpenAIApi(
    new Configuration({
        apiKey: process.env.OPEN_AI_API_KEY,
    })
)

app.get('/',(mreq,mres)=> {
    mres.render('index.html')
})

app.get('/prompt', async (mreq, mres) => {
    //ChatGPT call
    const user_data = mreq.query
    const PROMPT = `على ماذا تدل هذه الأعراض: الضغط الانقباضي/الانبساطي للمريض: ${user_data["blood_pressure"]}, درجة الحرارة للمريض: ${user_data["temp"]}, سكر المريض ${user_data["sugar"]}, و الأعراض ${user_data["symptoms"]}, علما بأن عمر المريض ${user_data["age"]}, جنس المريض ${user_data["gender"]}, طول المريض ${user_data["length"]}, وزن المريض ${user_data["weight"]} واخيرا اذكر بعض النصائح في مثل هذه الحالة واذكر ما قد يجب فعله و اذكر مستوى الخطر مرتفع او منخفض او متوسط`
    const response = await openAi.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: PROMPT }],
    })
    console.log(response.data.choices[0].message.content)

    mres.render('results.ejs', {results: response.data.choices[0].message.content});
})

app.listen(process.env.PORT || 80, () => console.log('Connected on port 80'))
