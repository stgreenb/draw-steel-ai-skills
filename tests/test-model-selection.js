/**
 * Model Selection Playwright MCP Tests
 * Tests for model dropdown, switching, and persistence functionality
 */

import { chromium } from 'playwright';

const BASE_URL = 'http://localhost:8081';
const USERNAME = 'admin';
const PASSWORD = 'admin';

async function login(page) {
    await page.goto(`${BASE_URL}/dashboard`);
    await page.fill('input[name="username"]', USERNAME);
    await page.fill('input[name="password"]', PASSWORD);
    await page.click('button[type="submit"]');
    await page.waitForSelector('#model-select');
}

async function testModelSelectorDropdown() {
    console.log('Testing model selector dropdown...');
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await login(page);

        // Verify model selector exists
        const modelSelect = await page.$('#model-select');
        if (!modelSelect) {
            throw new Error('Model selector dropdown not found');
        }
        console.log('✓ Model selector dropdown is visible');

        // Verify all three models are in dropdown
        const options = await page.$$('#model-select option');
        const modelNames = await Promise.all(options.map(opt => opt.textContent()));
        const expectedModels = ['claude-sonnet-4-5', 'gemini-3-flash', 'gpt-oss-120b'];
        for (const model of expectedModels) {
            if (!modelNames.includes(model)) {
                throw new Error(`Model ${model} not found in dropdown`);
            }
        }
        console.log('✓ All three models are in the dropdown');

        // Verify default selection
        const selectedValue = await page.$eval('#model-select', el => el.value);
        if (selectedValue !== 'claude-sonnet-4-5') {
            throw new Error(`Default model should be claude-sonnet-4-5, got ${selectedValue}`);
        }
        console.log('✓ Default selection is claude-sonnet-4-5');

        // Verify model information is displayed
        const modelInfo = await page.$('#model-info');
        if (!modelInfo) {
            throw new Error('Model information display not found');
        }
        const infoText = await modelInfo.textContent();
        if (!infoText.includes('Avg Time') || !infoText.includes('Avg Tokens')) {
            throw new Error('Model information does not contain expected metrics');
        }
        console.log('✓ Model information is displayed');

        console.log('✓ All model selector dropdown tests passed!');
    } catch (error) {
        console.error('✗ Test failed:', error.message);
        throw error;
    } finally {
        await browser.close();
    }
}

async function testModelSwitching() {
    console.log('Testing model switching between generations...');
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await login(page);

        // Select gpt-oss-120b
        await page.selectOption('#model-select', 'gpt-oss-120b');
        const selected1 = await page.$eval('#model-select', el => el.value);
        if (selected1 !== 'gpt-oss-120b') {
            throw new Error('Failed to select gpt-oss-120b');
        }
        console.log('✓ Selected gpt-oss-120b');

        // Generate a monster
        await page.fill('#idea-text', 'Level 1 Skeleton');
        await page.click('#generate-btn');
        await page.waitForSelector('#output-panel', { timeout: 60000 });
        console.log('✓ Generated monster with gpt-oss-120b');

        // Switch to gemini-3-flash
        await page.selectOption('#model-select', 'gemini-3-flash');
        const selected2 = await page.$eval('#model-select', el => el.value);
        if (selected2 !== 'gemini-3-flash') {
            throw new Error('Failed to switch to gemini-3-flash');
        }
        console.log('✓ Switched to gemini-3-flash');

        // Generate another monster
        await page.fill('#idea-text', 'Level 2 Zombie');
        await page.click('#generate-btn');
        await page.waitForSelector('#output-panel', { timeout: 60000 });
        console.log('✓ Generated another monster with gemini-3-flash');

        console.log('✓ All model switching tests passed!');
    } catch (error) {
        console.error('✗ Test failed:', error.message);
        throw error;
    } finally {
        await browser.close();
    }
}

async function testModelPersistence() {
    console.log('Testing model persistence across page loads...');
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await login(page);

        // Select gemini-3-flash
        await page.selectOption('#model-select', 'gemini-3-flash');
        const selected1 = await page.$eval('#model-select', el => el.value);
        if (selected1 !== 'gemini-3-flash') {
            throw new Error('Failed to select gemini-3-flash');
        }
        console.log('✓ Selected gemini-3-flash');

        // Generate a monster
        await page.fill('#idea-text', 'Level 3 Wraith');
        await page.click('#generate-btn');
        await page.waitForSelector('#output-panel', { timeout: 60000 });
        console.log('✓ Generated monster');

        // Refresh the page
        await page.reload();
        await page.waitForSelector('#model-select');

        // Verify model selector still shows gemini-3-flash
        const selected2 = await page.$eval('#model-select', el => el.value);
        if (selected2 !== 'gemini-3-flash') {
            throw new Error(`Model selection not persisted after refresh. Expected gemini-3-flash, got ${selected2}`);
        }
        console.log('✓ Model selection persisted after page refresh');

        console.log('✓ All model persistence tests passed!');
    } catch (error) {
        console.error('✗ Test failed:', error.message);
        throw error;
    } finally {
        await browser.close();
    }
}

// Run all tests
async function runAllTests() {
    console.log('Starting Model Selection Playwright MCP Tests...\n');

    try {
        await testModelSelectorDropdown();
        console.log();
        await testModelSwitching();
        console.log();
        await testModelPersistence();
        console.log();
        console.log('✅ All Model Selection tests passed successfully!');
    } catch (error) {
        console.error('\n❌ Tests failed:', error.message);
        process.exit(1);
    }
}

// Run tests if this file is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
    runAllTests().catch(error => {
        console.error('Test error:', error);
        process.exit(1);
    });
}

export { testModelSelectorDropdown, testModelSwitching, testModelPersistence, runAllTests };