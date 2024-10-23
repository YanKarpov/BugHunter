const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
    const { territory, proposal } = req.body;

    if (!territory || !proposal) {
        return res.status(400).json({ error: 'Территория и предложение обязательны!' });
    }

    console.log(`Получено предложение для территории: ${territory}`);
    console.log(`Предложение: ${proposal}`);

    return res.status(200).json({ message: 'Информация успешно собрана!' });
});


app.listen(PORT, () => {
    console.log(`Сервер запущен на http://localhost:${PORT}`);
});
