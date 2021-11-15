using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;  
using System.IO;

public class quotesGenerator : MonoBehaviour
{
    public Text txt;

    public void Click(){
	System.Random random = new System.Random(); 
	int num = random.Next(0,350);
	
	string[] quotes = System.IO.File.ReadAllLines("motivationSpeeches.txt");
	int i = quotes[num].IndexOf('-');

	if(quotes[num][0] == '\"' || quotes[num][0] == '\''){
		txt.text = quotes[num] + '\n';}
	else{
		txt.text = quotes[num+1] + '\n';}
}
}
