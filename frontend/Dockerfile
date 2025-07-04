FROM node:22-slim AS build
 
WORKDIR /app
COPY package*.json ./

RUN yarn install --production
 
COPY . .
#EXPOSE 3000
 
RUN yarn build
#CMD ["yarn", "build"]

FROM nginx 
COPY ./webserver/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/build /usr/share/nginx/html