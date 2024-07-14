const MODIFIER = BigInt(9824516953);
const SHIFT = BigInt(69540112799);
const KEY = BigInt(413276118390);
const MOD_VALUE = BigInt(65536);
const ROUNDS = 90000;
const BLOCK_SIZE = 16;

function hashFunction(value, round, extraKey) {
    let key = KEY + BigInt(extraKey.charCodeAt(round % extraKey.length));
    return (value * MODIFIER + BigInt(Math.floor(Math.sin(Number(key) + round) * 1000)) + SHIFT + BigInt(round)) % MOD_VALUE;
}

function doubleHashFunction(value, round, extraKey1, extraKey2) {
    let hashedValue = hashFunction(value, round, extraKey1);
    return hashFunction(hashedValue, round, extraKey2);
}

function reverseDoubleHashFunction(value, round, extraKey1, extraKey2) {
    let hashedValue = reverseHashFunction(value, round, extraKey2);
    return reverseHashFunction(hashedValue, round, extraKey1);
}

function reverseHashFunction(value, round, extraKey) {
    let key = KEY + BigInt(extraKey.charCodeAt(round % extraKey.length));
    return (value - SHIFT - BigInt(Math.floor(Math.sin(Number(key) + round) * 1000)) - BigInt(round) + MOD_VALUE) * modularInverse(MODIFIER, MOD_VALUE) % MOD_VALUE;
}

function modularInverse(a, mod) {
    let m0 = mod, t, q;
    let x0 = BigInt(0), x1 = BigInt(1);
    if (mod === BigInt(1)) return BigInt(0);
    while (a > BigInt(1)) {
        q = a / mod;
        t = mod;
        mod = a % mod, a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < BigInt(0)) x1 += m0;
    return x1;
}

function encrypt() {
    let inputText = document.getElementById("inputText").value;
    let extraKey1 = document.getElementById("extraKey1").value;
    let extraKey2 = document.getElementById("extraKey2").value;
    let charCodes = [];

    while (inputText.length % BLOCK_SIZE !== 0) {
        inputText += '\0';
    }

    for (let i = 0; i < inputText.length; i++) {
        let charCode = BigInt(inputText.charCodeAt(i));
        for (let round = 0; round < ROUNDS; round++) {
            charCode = doubleHashFunction(charCode, round, extraKey1, extraKey2);
        }
        charCodes.push(Number(charCode));
    }

    let uint16array = new Uint16Array(charCodes);
    let blob = new Blob([uint16array], {type: 'application/octet-stream'});
    let reader = new FileReader();
    reader.onload = function() {
        document.getElementById("result").innerText = "Encrypted Text: " + btoa(reader.result);
        updateHistory('Encrypt', inputText, btoa(reader.result));
    };
    reader.readAsBinaryString(blob);
}

function decrypt() {
    let inputText = atob(document.getElementById("inputText").value);
    let extraKey1 = document.getElementById("extraKey1").value;
    let extraKey2 = document.getElementById("extraKey2").value;
    let uint16array = new Uint16Array(inputText.length / 2);

    for (let i = 0; i < inputText.length; i += 2) {
        uint16array[i / 2] = inputText.charCodeAt(i) | (inputText.charCodeAt(i + 1) << 8);
    }

    let decryptedText = '';
    for (let i = 0; i < uint16array.length; i++) {
        let charCode = BigInt(uint16array[i]);
        for (let round = ROUNDS - 1; round >= 0; round--) {
            charCode = reverseDoubleHashFunction(charCode, round, extraKey1, extraKey2);
        }
        decryptedText += String.fromCharCode(Number(charCode));
    }

    decryptedText = decryptedText.replace(/\0+$/, '');
    document.getElementById("result").innerText = "Decrypted Text: " + decryptedText;
    updateHistory('Decrypt', document.getElementById("inputText").value, decryptedText);
}

function updateHistory(action, text, result) {
    let table = document.getElementById('historyTable').getElementsByTagName('tbody')[0];
    let newRow = table.insertRow();
    newRow.insertCell(0).textContent = action;
    newRow.insertCell(1).textContent = text;
    newRow.insertCell(2).textContent = result;
}

function togglePassphraseVisibility() {
    let passphraseInput = document.getElementById("passphrase");
    if (document.getElementById("showPassphrase").checked) {
        passphraseInput.type = "text";
    } else {
        passphraseInput.type = "password";
    }
}

function requestPassphrase(action) {
    let passphrase = document.getElementById("passphrase").value;
    if (passphrase.trim() === "" || passphrase.length !== 4) {
        alert("Please enter a 4-digit passphrase!");
        return;
    }
    if (action === 'export') {
        exportKeys();
    } else if (action === 'import') {
        importKeys();
    }
}

function exportKeys() {
    let extraKey1 = document.getElementById("extraKey1").value;
    let extraKey2 = document.getElementById("extraKey2").value;
    let keys = {
        extraKey1: extraKey1,
        extraKey2: extraKey2
    };
    document.getElementById("keys").value = JSON.stringify(keys);
    encryptKeys();
}

function importKeys() {
    decryptKeys();
    let keys = JSON.parse(document.getElementById("keys").value);
    document.getElementById("extraKey1").value = keys.extraKey1;
    document.getElementById("extraKey2").value = keys.extraKey2;
}

function encryptKeys() {
    let keys = document.getElementById("keys").value;
    let passphrase = document.getElementById("passphrase").value;
    if (keys.trim() === "" || passphrase.trim() === "" || passphrase.length !== 4) {
        alert("Please enter keys and a 4-digit passphrase!");
        return;
    }

    let charCodes = [];
    for (let i = 0; i < keys.length; i++) {
        let charCode = BigInt(keys.charCodeAt(i));
        for (let round = 0; round < ROUNDS; round++) {
            charCode = doubleHashFunction(charCode, round, passphrase, passphrase);
        }
        charCodes.push(Number(charCode));
    }
    let uint16array = new Uint16Array(charCodes);
    let blob = new Blob([uint16array], {type: 'application/octet-stream'});
    let reader = new FileReader();
    reader.onload = function() {
        document.getElementById("keys").value = btoa(reader.result);
    };
    reader.readAsBinaryString(blob);
}

function decryptKeys() {
    let keys = document.getElementById("keys").value;
    let passphrase = document.getElementById("passphrase").value;
    if (keys.trim() === "" || passphrase.trim() === "" || passphrase.length !== 4) {
        alert("Please enter encrypted keys and a 4-digit passphrase!");
        return;
    }

    let encodedText = atob(keys);
    let uint16array = new Uint16Array(encodedText.length / 2);
    for (let i = 0, j = 0; i < encodedText.length; i += 2, j++) {
        let charCode = BigInt(encodedText.charCodeAt(i) + (encodedText.charCodeAt(i + 1) << 8));
        for (let round = ROUNDS - 1; round >= 0; round--) {
            charCode = reverseDoubleHashFunction(charCode, round, passphrase, passphrase);
        }
        uint16array[j] = Number(charCode);
    }
    let result = '';
    for (let charCode of uint16array) {
        result += String.fromCharCode(charCode);
    }
    document.getElementById("keys").value = result;
}

function exportTable() {
    let table = document.getElementById('historyTable');
    let rows = [];
    for (let i = 1; i < table.rows.length; i++) {
        let row = [];
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            row.push(table.rows[i].cells[j].innerText);
        }
        rows.push(row);
    }
    let json = JSON.stringify(rows);
    encryptText(json, document.getElementById("passphrase").value).then(encrypted => {
        document.getElementById("keys").value = encrypted;
    });
}

function importTable() {
    let encrypted = document.getElementById("keys").value;
    decryptText(encrypted, document.getElementById("passphrase").value).then(decrypted => {
        let rows = JSON.parse(decrypted);
        let table = document.getElementById('historyTable').getElementsByTagName('tbody')[0];
        table.innerHTML = "";
        rows.forEach(row => {
            let newRow = table.insertRow();
            row.forEach(cell => {
                newRow.insertCell().textContent = cell;
            });
        });
    });
}

async function encryptText(text, passphrase) {
    if (passphrase.trim() === "" || passphrase.length !== 4) {
        alert("Please enter a 4-digit passphrase!");
        return "";
    }

    let charCodes = [];
    for (let i = 0; i < text.length; i++) {
        let charCode = BigInt(text.charCodeAt(i));
        for (let round = 0; round < ROUNDS; round++) {
            charCode = doubleHashFunction(charCode, round, passphrase, passphrase);
        }
        charCodes.push(Number(charCode));
    }
    let uint16array = new Uint16Array(charCodes);
    let blob = new Blob([uint16array], {type: 'application/octet-stream'});
    let reader = new FileReader();
    return new Promise((resolve) => {
        reader.onload = function() {
            resolve(btoa(reader.result));
        };
        reader.readAsBinaryString(blob);
    });
}

async function decryptText(encrypted, passphrase) {
    if (passphrase.trim() === "" || passphrase.length !== 4) {
        alert("Please enter a 4-digit passphrase!");
        return "";
    }

    let inputText = atob(encrypted);
    let uint16array = new Uint16Array(inputText.length / 2);
    for (let i = 0; i < inputText.length; i += 2) {
        uint16array[i / 2] = inputText.charCodeAt(i) | (inputText.charCodeAt(i + 1) << 8);
    }

    let decryptedText = '';
    for (let i = 0; i < uint16array.length; i++) {
        let charCode = BigInt(uint16array[i]);
        for (let round = ROUNDS - 1; round >= 0; round--) {
            charCode = reverseDoubleHashFunction(charCode, round, passphrase, passphrase);
        }
        decryptedText += String.fromCharCode(Number(charCode));
    }

    return decryptedText;
}

document.addEventListener('DOMContentLoaded', function() {
    let currentLang = localStorage.getItem('selectedLanguage') || 'en';

    function updateTexts() {
        document.getElementById('title').textContent = languages[currentLang].title;
        document.getElementById('encryptionDecryption').textContent = languages[currentLang].encryptionDecryption;
        document.getElementById('instructions').textContent = languages[currentLang].instructions;
        document.getElementById('instructionItem1').textContent = languages[currentLang].instructionItem1;
        document.getElementById('instructionItem2').textContent = languages[currentLang].instructionItem2;
        document.getElementById('memorablePassphrase').textContent = languages[currentLang].memorablePassphrase;
        document.getElementById('textToEncryptDecrypt').textContent = languages[currentLang].textToEncryptDecrypt;
        document.getElementById('inputText').placeholder = languages[currentLang].enterText;
        document.getElementById('extraKey1Label').textContent = languages[currentLang].extraKey1;
        document.getElementById('extraKey1').placeholder = languages[currentLang].enterKey1;
        document.getElementById('extraKey2Label').textContent = languages[currentLang].extraKey2;
        document.getElementById('extraKey2').placeholder = languages[currentLang].enterKey2;
        document.getElementById('encryptBtn').textContent = languages[currentLang].encrypt;
        document.getElementById('decryptBtn').textContent = languages[currentLang].decrypt;
        document.getElementById('keyExportImport').textContent = languages[currentLang].keyExportImport;
        document.getElementById('keys').placeholder = languages[currentLang].keysJSON;
        document.getElementById('passphraseLabel').textContent = languages[currentLang].passphrase;
        document.getElementById('passphrase').placeholder = languages[currentLang].enterPassphrase;
        document.getElementById('exportTableBtn').textContent = languages[currentLang].exportTable;
        document.getElementById('importTableBtn').textContent = languages[currentLang].importTable;
        document.getElementById('action').textContent = languages[currentLang].action;
        document.getElementById('text').textContent = languages[currentLang].text;
        document.getElementById('resultCol').textContent = languages[currentLang].result;
        document.getElementById('footer').textContent = languages[currentLang].footer;
        document.getElementById('github').textContent = languages[currentLang].github;
        document.getElementById('languageSelector').value = currentLang;
    }

    function changeLanguage(lang) {
        currentLang = lang;
        localStorage.setItem('selectedLanguage', lang);
        updateTexts();
    }

    updateTexts();

    document.getElementById('languageSelector').addEventListener('change', function() {
        changeLanguage(this.value);
    });
});