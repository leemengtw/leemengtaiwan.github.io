// tf.disableDeprecationWarnings();

let dropDownElement = document.getElementById("styles");
let inputImgElement = document.getElementById('input');
let appStatusElement = document.getElementById('app-status');
let outputElement = document.getElementById('output');
let preOutputElement = document.getElementById('pregenerated_output');


function logStatus(message) {
    appStatusElement.textContent = message;
    appStatusElement.style.display = 'block';
    outputElement.style.display = 'none';
    preOutputElement.style.display = 'none';
}


let generator;
async function setupGenerator(style) {

    const URL_PREFIX = 'https://raw.githubusercontent.com/leemengtaiwan/tfjs-models/master/cartoongan/';
    const MODEL_URL = URL_PREFIX + 'tfjs_json_models/' + style + '/model.json';
    console.log(MODEL_URL);
    generator = await tf.loadGraphModel(MODEL_URL);

    console.log('generator loaded.');
    console.log('warm up generator');
    generator.predict(tf.zeros([1, 1, 1, 3])).dispose();
    return generator;
}


async function predict(style, inputImgElement) {
    console.log("before predicting: ", tf.memory());

    let inputImgTensor = tf.browser.fromPixels(inputImgElement);
    inputImgTensor = inputImgTensor.toFloat();
    inputImgTensor = inputImgTensor.reverse(axis=2);
    inputImgTensor = tf.expandDims(inputImgTensor, 0);

    const startTime = performance.now();
    logStatus("Loading Model...");
    generator = await setupGenerator(style);

    logStatus("Cartoonizing images...");
    let generatedImgTensor = generator.predict(inputImgTensor);
    generatedImgTensor = tf.squeeze(generatedImgTensor, 0);
    generatedImgTensor = generatedImgTensor.reverse(axis=2);
    generatedImgTensor = generatedImgTensor.mul(0.5).add(0.5);
    console.log(generatedImgTensor);
    generatedImgTensor = tf.clipByValue(generatedImgTensor, 0, 1);
    renderResult(generatedImgTensor);
    inputImgTensor.dispose();

    const totalTime = performance.now() - startTime;
    console.log(`Transformation done in ${Math.floor(totalTime)}ms`);
    console.log("after predicting: ", tf.memory())
}


function renderResult(imgTensor) {
    tf.browser.toPixels(imgTensor, outputElement);
    preOutputElement.style.display = 'none';
    appStatusElement.style.display = 'none';
    outputElement.style.display = 'inline-block';
}


const filesElement = document.getElementById('files');
filesElement.addEventListener('change', evt => {
    console.log('input image changed.');
    const startTime = performance.now();
    const totalTime = performance.now() - startTime;
    console.log(`Done in ${Math.floor(totalTime)}ms`);

    let files = evt.target.files;
        // Display thumbnails & issue call to predict each image.

        // console.log("before: ", tf.memory());

        for (let i = 0, f; f = files[i]; i++) {
            // Only process image files (skip non image files)
            if (!f.type.match('image.*')) {
                continue;
            }
            let reader = new FileReader();
            const idx = i;
            // Closure to capture the file information.
            reader.onload = e => {
                let style = dropDownElement[dropDownElement.selectedIndex].value;
                let inputImgElement = document.getElementById('input');
                inputImgElement.src = e.target.result;
                inputImgElement.onload = () => predict(style, inputImgElement);
        };

        // Read in the image file as a data URL.
        reader.readAsDataURL(f);
    }
});

// monitor select value changes
// ref: http://jsfiddle.net/kyw2E/
document.getElementById("styles").onchange = function(e) {
    let style = this[this.selectedIndex].value;


    predict(style, inputImgElement);
};
