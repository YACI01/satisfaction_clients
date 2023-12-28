// Importez la bibliothèque Plotly
import Plotly from "plotly.js";

// Créez un objet Plotly
const myPlot = new Plotly.Plot();

// Chargez les données NDJSON dans l'objet Plotly
const data = require("./dashboard/dashboard.ndjson");

// Créez un graphique à partir des données NDJSON
myPlot.data.add({
  x: data.map(d => d.x),
  y: data.map(d => d.y),
});

// Appelez la méthode plot() de l'objet Plotly pour créer le graphique
myPlot.plot();
