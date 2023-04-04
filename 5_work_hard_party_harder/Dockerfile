FROM node:current-alpine

WORKDIR /app
COPY ["./is_eternal/package.json", "./is_eternal/package-lock.json*", "./is_eternal/public", "./"]
RUN npm install
EXPOSE 8080
CMD [ "npm", "start" ]