const { Octokit } = require('@octokit/rest');

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN,
});

const owner = process.env.GITHUB_REPOSITORY_OWNER;
const repo = process.env.GITHUB_REPOSITORY;

const issueTitle = 'Failure in CI - Module Name';
const issueBody = 'Se han encontrado errores en la ejecución de tests. ¡Por favor, verifica y soluciona el problema!';

async function createIssue() {
  try {
    const newIssue = await octokit.issues.create({
      owner,
      repo,
      title: issueTitle,
      body: issueBody,
    });
    console.log(`Se ha creado un nuevo issue: ${newIssue.data.html_url}`);
  } catch (error) {
    console.error('Hubo un error al crear el issue:', error);
  }
}

createIssue();
