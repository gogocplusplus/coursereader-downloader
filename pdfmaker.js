const puppeteer = require('puppeteer');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
const { exec } = require('child_process');

let getPromptInput = (question) => {
    return new Promise((resolve) => {
        readline.question(question, (answer) => {
            resolve(answer);
        });
    });
}

const createPdf = async () => {
    const baseUrl = await getPromptInput('Enter the base url: ');
    const baseFileName = await getPromptInput('Enter the base file name: ');
    let layout = await getPromptInput('Enter the layout (portrait, landscape; default is landscape): ');
    let landscape = layout === 'portrait' ? false : true;
    let format = await getPromptInput('Enter the format (A3, A4, Letter, Legal, Tabloid; default is A4): ');
    format = format === '' ? 'A4' : format;
    let scale = await getPromptInput('Enter the scale value (0.1 - 1, default is 0.55): ');
    scale = scale === '' ? 0.55 : parseFloat(scale);


    const browser = await puppeteer.launch({headless: 'new'});
    const page = await browser.newPage();

    await page.goto(baseUrl, { waitUntil: 'networkidle2'});

    // Extract the href attribute from each link
    let links = await page.$$eval('.link.inactive, .link.active', anchors => {
        return anchors.map(anchor => anchor.href);
    });

    let index = 0;
    for (let link of links) {
        const tempPage = await browser.newPage();
        await tempPage.goto(link, { waitUntil: 'networkidle2'});
        await tempPage.emulateMediaType('screen');
        await tempPage.addStyleTag({content: `body { text-align: center; }`});

        const options = {
            path: `pdf/${baseFileName}-${String.fromCharCode(97 + index)}.pdf`, // 97 is ASCII value for 'a'
            format: format,
            printBackground: true,
            landscape: landscape,
            scale: scale,
            margin: {
                top: "0.25cm",
                right: "1cm",
                left: "1cm"
            }
        }

        await tempPage.pdf(options);
        await tempPage.close();
        index += 1;
    }

    await browser.close();
    readline.close();

    // Use source instead of call on Linux
    exec('call ./venv/scripts/activate && python pdfcombiner.py', (err, stdout, stderr) => {
        if (err) {
            console.error(`exec error: ${err}`);
            return;
        }
        console.log(`Python script output:\n${stdout}`);
    });
};

createPdf();
