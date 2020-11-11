package main 

import (
	"fmt"
	scp "github.com/bramvdbogaerde/go-scp"
	"github.com/bramvdbogaerde/go-scp/auth"
	"golang.org/x/crypto/ssh"
	"os"
)

func main() {
	// use SSH key auth from auth package 
	// we ignore host key in this ex. but ignore this if you use this library 
	clientConfig, _ := auth.PrivateKey("username", "/path/to/rsa/key", ssh.InsecureIgnoreHostKey())

	// for other auth methods see ss.ClientConfig and ssh.AuthMethod
	// create new scp client 
	client := scp.NewClient("example.com:22", &clientConfig)

	// connect to remote server 
	err := client.Connect()
	if err != nil {
		fmt.Println("could not establish connection to remote server ", err)
		return 
	// above is merely to connect to system 
	// if already have ssh connection would use different method - https://github.com/bramvdbogaerde/go-scp#using-an-existing-ssh-connection
	// open a file 
	f, _ := os.Open("/path/to/local/file")
	
	// close client connection after file has been copied 
	defer client.Close()
	
	// close the file after it has been copied 
	defer f.Close()
	
	// copy file over, CopyFile(fileReader, remotePath, permission)
	err = client.CopyFile(f, "/home/server/test.txt", "0655")
	
	if err != nil {
		fmt.Println("Error while copying file ", err)
	}
}
