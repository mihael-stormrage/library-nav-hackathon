import path from 'path';
import request from 'request';
import bodyParser from 'body-parser';
import express from 'express';
import exphbs from 'express-handlebars';
// import {PythonShell} from 'python-shell';

const app = express();

const __dirname = path.resolve();
const apiUrl = 'http://poisk.ngonb.ru/opacg.integration.smev/STORAGE/opacfindd/FindView/2.3.0';

app.engine('.hbs', exphbs({
  defaultLayout: 'main',
  extname: '.hbs',
  layoutsDir: path.join(__dirname, 'views/layouts')
}));
app.use(express.static('views/images'));

app.set('view engine', '.hbs');
app.set('views', path.join(__dirname, 'views'));
app.listen(3000);

app.use('/form_handler', bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

app.post('/form_handler', function (req, res, next) {

  const place = {
    floor: 0,
    room: 0,
    stand: 0,
    shelf: 0
  };

  // Объект req.body содержит данные из переданной формы
  request.post({
    url: apiUrl,
    json: true,
    body: req.body
  }, (err, response, body) => {
    if (err)
      return res.status(500).send({message: err});

    console.log(body);
    res.render('place', {
      placePic: "f1ga2343h4bc3.png"
    });
    // console.log(JSON.parse(body.toString()).maxLastResult);
    // return res.send(body);
    // return response;
  });

  // const shell = new PythonShell('main.py', { mode: 'json'});
  // shell.send(place);

});

app.get('/', (request, response) => {
  response.render('home', {
    apiUrl: apiUrl
  });
});