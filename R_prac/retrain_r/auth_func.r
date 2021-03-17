library("httr")
library("jsonlite")

#  Get Client Token
#  Parameters: 
#     - host = hostname 
#     - consul_token (get on your SAS Server on this path: 
#     /opt/sas/viya/config/etc/SASSecurityCertificateFramework/tokens/consul/default/client.token)
#  Outputs:
#     - This call will generate a token, save it for the next call (where it says 'token_from_call_above')

#  Call: 

get_access_token <- function(host, consul_token, verbose = FALSE) {
  
  url <- parse_url(host)
  url$path <- "/SASLogon/oauth/clients/consul"
  url$query <- list(
    "callback" = "false",
    "serviceId" = "app"
  )
  
  response <- POST(
    url = build_url(url),
    add_headers(
      "X-Consul-Token"= consul_token
    ),
    
    if(verbose) verbose()
  )
  
  stop_for_status(response)
  idToken <- fromJSON(content(response, as = "text"))
  return(idToken)
  
}


#  Register Client
#  Parameters: 
#     - host = hostname
#     - idToken = access token from consul idToken$access_token
#     - client_name
#     - client_secret
#  Outputs:
#      - It will return the client created

# Call:

register_client <- function(host, idToken, client_name, client_secret, 
                            verbose = FALSE, scope = "openid") {
  
  url <- parse_url(host)
  url$path <- "/SASLogon/oauth/clients"
  
  body <- list(
    "client_id" = client_name,
    "scope" = scope,
    "access_token_validity" = 36000,
    "client_secret" = client_secret,
    "resource_ids" = "none",
    "authorities" = "uaa.none",
    "authorized_grant_types"= "password"
  )
  
  response <- POST(
    url = build_url(url),
    add_headers(
      "Content-Type"="application/json",
      "authorization" = paste("Bearer", idToken)
    ),
    body = toJSON(body, auto_unbox = T),
    if(verbose) verbose()
  )
  
  stop_for_status(response)
  registered_client <- fromJSON(content(response, as = "text"))
  return(registered_client)
}

url <- "http://magnus.unx.sas.com/SASLogon/oauth/token?grant_type=password&username=demo&password=Orion123"
response <- GET(url,add_headers(.headers = c("accept"= 'application/json',"Authorization"='Basic cl9jbGllbnQzOnJfc2VjcmV0',"Content-Type"="application/x-www-form-urlencoded")),verbose())
content(response, 'parsed')
