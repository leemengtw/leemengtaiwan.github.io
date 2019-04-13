import * as tf from '@tensorflow/tfjs';
import {INDEX2WORD} from './dictionary';
import {WORD2INDEX} from './dictionary';
import {SEEDS} from './text';


const appStatus = document.getElementById('app-status');
const textGenerationStatus = document.getElementById('text-generation-status');

const loadModelButton = document.getElementById('load-model');
const initializeSeedButton = document.getElementById('initialize-seed');
const generateTextButton = document.getElementById('generate-text');

const generateLengthInput = document.getElementById('generate-length');
const temperatureInput = document.getElementById('temperature');
const seedTextInput = document.getElementById('seed-text');
const generatedTextInput = document.getElementById('generated-text');

const sampleLen = 30;
let model;


function logStatus(message) {
  appStatus.textContent = message;
}

export function onTextGenerationBegin() {
    generatedTextInput.value = '';
    logStatus('生成文章中 ...');
}

export function onLoadModelBegin() {
    logStatus('LSTM 神經網路加載中 ...');
}

export function onLoadModelEnd() {
    logStatus('LSTM 神經網路已成功載入');
}

export function sample(probs) {
    return tf.tidy(() => {
        const temperature = parseFloat(temperatureInput.value);
        const logits = tf.div(probs, Math.max(temperature, 1e-6));
        const isNormalized = false;
        const seed = null;
        const generatedIndices = tf.multinomial(logits, 1, seed, isNormalized).dataSync();
        return generatedIndices[generatedIndices.length - 1]
    });
}

// export function sampleDev(logits) {
//     return tf.tidy(() => {
//
//         const temperature = parseFloat(temperatureInput.value);
//         const isNormalized = false;
//         const seed = null;
//         var probs = tf.softmax(logits);
//         probs = tf.div(tf.log(probs), temperature);
//         probs = tf.exp(probs);
//         probs = tf.div(probs, probs.sum(1, true));
//         const generatedIndices = tf.multinomial(probs, 1, seed, isNormalized).dataSync();
//         return generatedIndices[generatedIndices.length - 1]
//     });
// }


export async function onTextGenerationChar(char) {
    generatedTextInput.value += char;
    generatedTextInput.scrollTop = generatedTextInput.scrollHeight;
    // const charCount = parseInt(generatedTextInput.value.length) - parseInt(seedTextInput.value.length);
    const charCount = generatedTextInput.value.length;
    const generateLength = parseInt(generateLengthInput.value);
    const status = `生成文章： ${charCount} / ${generateLength} 字 ...`;
    logStatus(status);
    textGenerationStatus.textContent = status;
    await tf.nextFrame();
}

export function loadModel() {
    model = tf.loadLayersModel("http://localhost:8765/lstm_1024units_512emb_100seqlen_128bsize_0.001lr/model.json");
    // model = tf.loadLayersModel("http://localhost:8765/lstm_512units_256emb_100seqlen_128bsize_0.001lr/model.json");
    // model = tf.loadLayersModel("https://raw.githubusercontent.com/leemengtaiwan/tfjs-models/master/text-generation/lstm_1024units_512emb_100seqlen_128bsize_0.001lr/model.json");
    return model;
}

export function initializeSeed() {
    const randIndex = Math.floor(Math.random() * SEEDS.length);
    const seedText = SEEDS[randIndex];
    seedTextInput.value = seedText;
    return seedText
}

export async function generateText() {
    let seedSentence;
    let seedSentenceIndices = [];

    seedSentence = seedTextInput.value;
    if (seedSentence.length == 0) {
        seedSentence = initializeSeed();
    }
    else if (seedSentence.length > sampleLen) {
        seedSentence = seedSentence.slice(
            seedSentence.length - sampleLen, seedSentence.length);
    }

    for (let i = 0; i < seedSentence.length; ++i) {
        seedSentenceIndices.push(WORD2INDEX[seedSentence[i]]);
    }

    let generated = '';
    const generateLength = parseInt(generateLengthInput.value);

    let inputEval = tf.tensor(seedSentenceIndices);
    model.resetStates();
    // generatedTextInput.value += seedSentence;
    while (generated.length < generateLength) {

        var input = inputEval;
        input = tf.expandDims(inputEval, 0);
        const output = model.predict(input);

        const sampledIndex = sample(tf.squeeze(output), temperature);
        const sampledChar = INDEX2WORD[sampledIndex];
        if (onTextGenerationChar != null) {
            await onTextGenerationChar(sampledChar);
        }

        if (typeof sampledChar !== 'undefined') {
            generated += sampledChar;
        }

        seedSentenceIndices = seedSentenceIndices.slice(1);
        seedSentenceIndices.push(sampledIndex);
        inputEval = tf.tensor(seedSentenceIndices);

        input.dispose();
        output.dispose();

    }

    generatedTextInput.innerText = generated;
    return await generated;
}

loadModelButton.addEventListener('click', async () => {
    onLoadModelBegin();
    loadModelButton.disabled = true;
    model = await loadModel();
    generateTextButton.disabled = false;
    initializeSeedButton.disabled = false;
    onLoadModelEnd();

});

initializeSeedButton.addEventListener('click', async () => {
    initializeSeed();
});

generateTextButton.addEventListener('click', async () => {
    onTextGenerationBegin();
    generateText();
});


// initializeSeed();
