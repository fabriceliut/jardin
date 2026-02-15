FROM ruby:3.2-slim

WORKDIR /srv/jekyll

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  git \
  nodejs \
  npm \
  curl \
  && rm -rf /var/lib/apt/lists/*

COPY Gemfile* ./
RUN gem install bundler && bundle install || true

# Install yarn via npm (deb package not always available in slim images)
RUN npm install -g yarn || true

COPY . ./

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--livereload"]
