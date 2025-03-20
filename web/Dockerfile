FROM node:20.17.0

WORKDIR /app

RUN npm cache clean --force
RUN npm init -y
RUN npm install -g npm
RUN apt-get update -qq && npm install -g vue-cli

# COPY .. :

# ENTRYPOINT ["npm", "run", "dev"]

RUN apt-get update -qq && yarn global add @vue/cli
RUN npm install yarn -g --force


COPY .. :

RUN yarn
CMD ["yarn", "dev", "--port", "3000"]
# RUN tail /dev/null
# docker compose build --no-cache