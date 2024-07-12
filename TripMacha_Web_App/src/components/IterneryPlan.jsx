import React, { useEffect, useRef, useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faList, faThumbsUp, faBookmark, faThumbsDown } from '@fortawesome/free-solid-svg-icons'
import { faBookmark as faBookmarkSlash } from '@fortawesome/free-regular-svg-icons'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Iterneries from './Iterneries';
import Iterneries_2 from './Iterneries_2';
import Iterneries_3 from './Iterneries_3';
import { useAuth } from '../context/AuthContext'

const IterneryPlan = () => {
  const {
    authUser,

    userPlaceName,
    userWithinRadius,
    userFromTime,
    userToTime,
    setUserPlaceName,
    setUserWithinRadius,
    setUserFromTime,
    setUserToTime,

    response1,
    response2,
    response3,
  } = useAuth();

  useEffect(() => {
    if (response1)
      console.log(response1);
  })



  const [isHidden1, setIsHidden1] = useState(false);
  const [isHidden2, setIsHidden2] = useState(false);
  const [isHidden3, setIsHidden3] = useState(false);

  const [bgColor1, setBgColor1] = useState('white');
  const [bgColor2, setBgColor2] = useState('white');
  const [bgColor3, setBgColor3] = useState('white');

  const [txtColor1, setTxtColor1] = useState('black');
  const [txtColor2, setTxtColor2] = useState('black');
  const [txtColor3, setTxtColor3] = useState('black');

  const [likeIcon1, setLikeIcon1] = useState(faThumbsUp);
  const [savedIcon1, setSavedIcon1] = useState(faBookmark);

  const liked1 = () => {
    if (likeIcon1 === faThumbsUp) {
      setLikeIcon1(faThumbsDown);
      toast('Iternery Liked!', {
        position: "top-center",
        autoClose: 1000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    } else {
      setLikeIcon1(faThumbsUp);
      toast('Iternery Disliked!', {
        position: "top-center",
        autoClose: 1000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  const saved1 = () => {
    if (savedIcon1 === faBookmark) {
      setSavedIcon1(faBookmarkSlash);
      toast('Iternery Saved!', {
        position: "top-center",
        autoClose: 1000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    } else {
      setSavedIcon1(faBookmark);
      toast('Iternery Unsaved!', {
        position: "top-center",
        autoClose: 1000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  // Iternery 2
  const [likeIcon2, setLikeIcon2] = useState(faThumbsUp);
  const [savedIcon2, setSavedIcon2] = useState(faBookmark);

  const liked2 = () => {
    if (likeIcon2 === faThumbsUp) {
      setLikeIcon2(faThumbsDown);
      toast('Iternery Liked!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    } else {
      setLikeIcon2(faThumbsUp);
      toast('Iternery Disliked!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  const saved2 = () => {
    if (savedIcon2 === faBookmark) {
      setSavedIcon2(faBookmarkSlash);
      toast('Iternery Saved!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    } else {
      setSavedIcon2(faBookmark);
      toast('Iternery Unsaved!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  // Iternery 3
  const [likeIcon3, setLikeIcon3] = useState(faThumbsUp);
  const [savedIcon3, setSavedIcon3] = useState(faBookmark);

  const liked3 = () => {
    if (likeIcon3 === faThumbsUp) {
      setLikeIcon3(faThumbsDown);
      toast('Iternery Liked!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    } else {
      setLikeIcon3(faThumbsUp);
      toast('Iternery Disliked!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };

  const saved3 = () => {
    if (savedIcon3 === faBookmark) {
      setSavedIcon3(faBookmarkSlash);
      toast('Iternery Saved!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    } else {
      setSavedIcon3(faBookmark);
      toast('Iternery Unsaved!', {
        position: "top-center",
        autoClose: 2000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
        theme: "dark",
      });
    }
  };


  return (
    <>
      <ToastContainer />

      {/* Iternery Section Starts */}
      <div className="container-xxl py-5">
        <div className="container">
          <div className="text-center">
            <h6 className="section-title text-center px-3 fs-3" style={{ color: "#37249D" }}>Your Trip Iternaries</h6>
            <h2 className="mb-5">Here are the Iternaries for a quick trip plan</h2>
          </div>

          <div className="row g-4">

            {/* Itenary plan 1 */}
            <div className="col-lg-4 col-sm-6" style={{left:'35%'}}>
              <div className="iternery-item rounded pt-3" style={{ backgroundColor: bgColor1, color: txtColor1 }}
                onClick={() => {
                  if (bgColor1 == 'white') {
                    setTxtColor1('white');
                    setTxtColor2('black');
                    setTxtColor3('black');
                    setBgColor1('#37249D');
                    setBgColor2('white');
                    setBgColor3('white');
                  }
                  else {
                    setTxtColor1('black');
                    setTxtColor2('black');
                    setTxtColor3('black');
                    setBgColor1('white');
                    setBgColor2('white');
                    setBgColor3('white');
                  }
                  setIsHidden1(!isHidden1)
                  setIsHidden2(false)
                  setIsHidden3(false)
                }}>
                <div className="p-4">
                  <p className="text-center fs-5"><FontAwesomeIcon icon={faList} />&nbsp;&nbsp;Best Iternery Plan</p>
                  <p className='text-center mt-4'>Places to visit: <span>Temples, Beaches, Restaurant</span></p>
                  <hr />
                  <div className='mb-4 mt-3'>
                    {
                      (authUser?.isAnonymous === true) ?
                        (<div className='float-right' onClick={liked1}><FontAwesomeIcon icon={likeIcon1} />&nbsp;&nbsp;{(likeIcon1 === faThumbsUp) ? <>Like</> : <>Dislike</>}</div>)
                        : (
                          <>
                            <div className='float-right' onClick={liked1}><FontAwesomeIcon icon={likeIcon1} />&nbsp;&nbsp;{(likeIcon1 === faThumbsUp) ? <>Like</> : <>Dislike</>}</div>
                            <div className='float-left' onClick={saved1}><FontAwesomeIcon icon={savedIcon1} />&nbsp;&nbsp;{(savedIcon1 === faBookmark) ? <>Save Plan</> : <>Unsave Plan</>}</div>
                          </>
                        )
                    }
                  </div>
                </div>
              </div>
            </div>

         
          </div>
        </div>
      </div>
      {/* Iternary Section Ends */}

      {isHidden1 && <Iterneries/>}
      {isHidden2 && <Iterneries_2 />}
      {isHidden3 && <Iterneries_3 />}
    </>
  )
}

export default IterneryPlan