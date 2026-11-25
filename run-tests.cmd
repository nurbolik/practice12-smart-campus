@echo off
cd /d "%~dp0"
echo === CODE-BASED TESTS ===
node --test --test-reporter=spec code\tests\rule.test.mjs
echo === LOW-CODE TESTS ===
node --test --test-reporter=spec lowcode\tests\engine.test.mjs
