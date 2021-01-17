def adventure():
  print("Choose your adventure...\n")
  print("""You are sitting in front of the computer and thinking about writing
a "choose your own adventure" game. What do you do?

1. Spend the next 5 minutes planning a story for the game.
2. Check your phone to see if there are any unread messages.\n""")
  choice = int(input(),10)
  if(choice == 1):
    print("""\n2 minutes into the thinking, you suddenly realized that you can write
about your own situation.

1. Proceed to start writing about a person who is trying to write a
"choose your own adventure" game.
2. Nah, that's lame.\n""")
    choice = int(input(),10)
    if (choice == 1):
      print("""\nYou started to write but ideas aren't flowing, apparently there is a dam
that is blocking the river flow. There is a name for the dam too, it's called
"dam, that's lame".

1. Snap the dam out of the existence and proceed to squeeze your ideas out 
like an overspent toothpaste.
2. Doubt yourself on whether you should continue writing about it\n""")
      choice = int(input(),10)
      if choice==1:
        print("""\n5 more minutes of writing, you began to wonder, should I write logically or 
imaginatively?

1. Logic prevails!
2. Realizes that logic starts with the letter "L" and you don't want to take 
another L in your life: I choose imagination!\n""")
        choice = int(input(),10)
        if choice == 1:
          print("""\nYou are finally done writing. With a dose of logic, the adventure script sounds
more plausible but lacks creativity. Perhaps there needs to be a healthy balance
of the two to make a more interesting storyline. But then you realized you have
done it and gave yourself a pad in the back. You stare at the screen and says
"Thanks for reading." END""")
        else:
          print("""\nWith imagination, you have a much easier time writing but unfortunately what
you wrote doesn't make a lot of sense. You couldn't figure out the central idea
of the script. 

1. Restart from scratch. Use logic this time.
2. Keep on writing. It's the effort that counts!\n""")
          choice = int(input(),10)
          if choice == 1:
            print("""\n
Your patience ran out and you quickly decide to take a break. Maybe you will
finish this another time. END""")
          else:
            print("""\nDespite the messey transition and confused logic, you managed to write a script
that is innovative in imagination but whoever understands this is either a 
telepathic genius or... someone who is reading this right now! END""")
      else:
        print("\nYou shouldn't have doubted yourself. You missed the opportunity to finish it. END")
    else:
      print("""\nYou tossed the idea out of your mind, what are you thinking now?

1. Write about a casual island survival story.
2. Write about a rags to riches story.\n""")
      choice = int(input(),10)
      if choice==1:
        print("""\nNothing spectacular: a few options and a short story, you did it. END""")
      else:
        print("""\nTook a little imagination and little research to make it plausible. But 
you got it done. END""")
  else: 
    print("""\nNo unread messages. You stare back at the screen, thinking: "Perhaps if I check
back in another 5 minutes, there might be >=1 unread messages!" Are you going to
follow your heart or remain at where you are?

1. Follow your heart, wait another 5 minutes and check your phone again.
Might get some work done in this 5 minutes too.
2. Remain. Don't wanna temper with desire at this moment. Gotta focus!\n""")
    choice = int(input(),10)
    if choice == 1:
      print("""\n5 minutes passed like a breeze. Hah, you thought. It was an excruciatingly
painful wait to another 5 minutes. You were distracted by the constant 
thought of checking on your phone and didn't make any progress in writing.
Finally, it's 5 minutes and you turn on the screen again, nothing.

1. You don't wanna waste another 5 minutes again. It's time to get this done.\n""")
      choice = int(input(),10)
      if choice == 1:
        print("""\n5 more minutes of writing, you began to wonder, should I write logically or 
imaginatively?

1. Logic prevails!
2. Realizes that logic starts with the letter "L" and you don't want to take 
another L in your life: I choose imagination!\n""")
        choice = int(input(),10)
        if choice == 1:
          print("""\nYou are finally done writing. With a dose of logic, the adventure script sounds
more plausible but lacks creativity. Perhaps there needs to be a healthy balance
of the two to make a more interesting storyline. But then you realized you have
done it and gave yourself a pad in the back. You stare at the screen and says
'Thanks for reading.'""")
        else:
          print("""\nWith imagination, you have a much easier time writing but unfortunately what
you wrote doesn't make a lot of sense. You couldn't figure out the central idea
of the script.
          
1. Restart from scratch. Use logic this time.
2. Keep on writing. It's the effort that counts!\n""")
          choice = int(input(),10)
          if choice == 1:
            print("""\n
Your patience ran out and you quickly decide to take a break. Maybe you will
finish this another time. END""")
          else:
            print("""\nDespite the messey transition and confused logic, you managed to write a script
that is innovative in imagination but whoever understands this is either a 
telepathic genius or... someone who is reading this right now! END""")
    else:
      print("""\nYou forced yourself to remain concentrated yet when god created mankind he forgot
to give you the trait "unwavering focus", you soon find yourself distracted again:
you feel compelled to quit writing and start relaxing.

1. Slap yourself in the face and keep on writing.
2. Be kind to yourself and allow yourself some respite.\n""")
      choice = int(input(),10)
      if choice==1:
        print("""\nIt is done. It took about half an hour to finish everything. The moment of relief
is soon overwhelmed with the sense of pain all around your body. You realized
you had to leash the inner demon with bodily torment. You looked at yourself
in the mirror and saw a bloated face. Is that still you? A period of silence,
out of nowhere you spoke: "glad you made it to the end." END""")
      else:
        print("""\nYou got the work done after the break. Wise choice. END""")

          



adventure()
  