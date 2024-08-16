# mlflow-server-gcp

Files to deploy mlflow server on GCP. Code for the blog post here - https://sambhav300899.github.io/blog/mlflow-on-gcp-2/

## Usage - 
1. Fork and pull
2. Add your own `GOOGLE_APPLICATION_CREDENTIALS` for your service account under `repo>settings>security>Secrets and Variables>Actions>Repository Secrets`
3. Update env variables in `.github/workflows/deploy_cloud_run.yml`
4. Push it!

## References - 
- https://medium.com/@andrevargas22/how-to-launch-an-mlflow-server-with-continuous-deployment-on-gcp-in-minutes-7d3a29feff88
- https://dlabs.ai/blog/a-step-by-step-guide-to-setting-up-mlflow-on-the-google-cloud-platform/

