master the launch of a full-fledged web application from different repositories. The application must contain frontend and backend parts from the corresponding repositories. The compose file must run the database for the application, and the nginx reverse proxy

1. Images should be lightweight
2. Use basic lightweight images - alpine
3. Consider running `backend`, `frontend`, `db` and `nginx-proxy`
4. All configuration is done through environment variables passed through `env_file` and `environment`
5. The entry point is only `nginx-proxy`, other services do not have ports open to the outside
6. It should be possible to configure through settings files in the form of `volume`
7. Containers must be run as an unprivileged user
8. After installing all the necessary utilities, the cache should be cleared