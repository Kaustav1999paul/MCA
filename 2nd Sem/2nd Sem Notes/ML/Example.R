# Show PWD
getwd()

# Print message
message <- "Hello world"
print(message)

# Print message
a <- 10
print(a)

# Show build in data-set
data(iris)
iris

tail(iris)
head(iris)
names(iris)


# Gives the values
min(iris$Sepal.Length)
mean(iris$Sepal.Length)
median(iris$Sepal.Width)
quantile(iris$Petal.Width)

summary(iris)


pa <- iris$Petal.Length
pb <- iris$Petal.Width
plot(pa, pb, pch=8, col="red")



speciesID <- as.numeric(iris$Species)
speciesID

plot(pa, pb, pch=speciesID, col=speciesID)

getws()
library(RTextTools)
library(tm)
library(wordcloud)

text <- readline(file.choose())
docs <- Corpus(VectorSource(text))
docs <- tm_map(docs, tolower)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, stemDocument)


dts <- TermDocumentMatrix(docs)
dts
m <- as.matrix(dts)
v <- sort(rowSums(m), decreasing = TRUE)
d <- data.frame(word= names(v), freq=v)
d
head(d, 10)
wordcloud(d$word, freq=d$freq, min.freq=1, max.word=40, random.order=FALSE, rot.per=0.35, color=brewer.pal(8, "Dark2"))






